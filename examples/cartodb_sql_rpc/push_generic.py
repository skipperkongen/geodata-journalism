from geopy import geocoders
import httplib
import urllib2, urllib
import sys
import pdb
import random

def main(options, args):

	print "Geocoding", options.loc	
	# Using geocoders: https://code.google.com/p/geopy/wiki/GettingStarted
	g = geocoders.GoogleV3()
	for place, (lat, lng) in g.geocode( options.loc, exactly_one=False ):
		print "%s: %.5f, %.5f" % (place, lat, lng)
	
	#lat += (random.random() - 0.5) * 0.001
	#lng += (random.random() - 0.5) * 0.01
	
	print "Pushing message to CartoDB observations"
	conn = httplib.HTTPSConnection("skipperkongen.cartodb.com")
	name, desc, api_key = options.name, options.desc, options.api_key
	print name,desc
	sql = \
		"INSERT INTO generisk_geodata(the_geom, name, description) \
		VALUES (ST_GeomFromText('POINT(%.5f %.5f)',%d),'%s','%s')" \
		% (lng, lat, 4326, name, desc)

	print sql
	path = "/api/v2/sql?q=%s&api_key=%s" % (urllib.quote_plus(sql), api_key)
	#sys.exit(0)
			
	conn.request("GET", path)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	print data
	
if __name__ == '__main__':
	from optparse import OptionParser
	usage = "usage: %prog [options] message"
	parser = OptionParser(usage=usage)
	parser.add_option("-a", "--api-key", dest="api_key", help="CartoDB api key")
	parser.add_option("-l", "--location", dest="loc", help="location string to geocode, e.g. an address")
	parser.add_option("-n", "--name", dest="name", help="Name of thing")
	parser.add_option("-d", "--description", dest="desc", help="Description of thing")
	(options, args) = parser.parse_args()
	
	main(options, args)