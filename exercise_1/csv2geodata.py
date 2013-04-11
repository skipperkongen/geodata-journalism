#!/usr/bin/env python

from optparse import OptionParser
import csv
import sys
import geojson
from geopy import geocoders
import pdb

def main(location_field, input, output):
	
	features = []
	id = 1
	geocoder = geocoders.GoogleV3()
	with open(input, 'rb') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		try:
			for row in reader:
				print "Geocoding",row[location_field],"... picking last coordinate"
				for place, (lat, lng) in geocoder.geocode( row[location_field], exactly_one=False ):
						print "\t%.5f, %.5f" % (lat, lng)
				# Create GeoJSON feature
				# pdb.set_trace()
				ft = geojson.Feature(id=id,geometry=geojson.Point([lat,lng]),properties=row)
				id += 1
				features.append( ft )
		except KeyError:
			print "Are you sure you're using the right fieldname? '%s' seems to an be invalid field name" % location_field
			sys.exit(0)
		except:
			print "Error parsing file"
			sys.exit(0)
	with open(output, 'w') as outfile:
		outfile.write(geojson.dumps(geojson.FeatureCollection(features)))
	print "Done writing result to",output

if __name__ == '__main__':
	
	usage="usage: python %prog [options] CSV-file"
	
	parser = OptionParser(usage=usage)
	parser.add_option("-l", "--location-field", dest="location_field",
					  help="Field in CSV-file containing a location that can be geocoded, e.g. an address")
	parser.add_option("-o", "--output", dest="output",default="output.json",
					  help="Filename to write GeoJSON result to, default is output.json")
	
	(options, args) = parser.parse_args()
	main(options.location_field, args[0], options.output)