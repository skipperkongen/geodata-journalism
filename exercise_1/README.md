# Fra [stuff] til geodata

**Problem**: Vi har en tekst-fil (CSV) med adresser på Apple-shops nær København. Vi vil gerne have en geodata fil (GeoJSON), som vi kan bruge til at vise butikkerne på et kort.

Data:

```csv
"APPLE_SHOP","ADRESSE"
"Humac A/S","Åboulevarden 15, 1960 Frederiksberg"
"Eplehuset A/S","Frederiksborggade 8, 1360 København K"
"Humac A/S","Gammel Mønt 12, 1117 København K"
"Humac A/S","Vesterbrogade 12, 1620 København V"
"Humac A/S","Lyngby Hovedgade 47, 2800 Lyngby"
"Kullander","Fridhemstorget 1, 21753 Malmö"
"MStore Malmö","Baltzarsgatan 26, 21136 Malmö"
"Humac A/S","Slotsarkaderne 1, 3400 Hillerød"
```

**Løsning**: Brug et Python program til at konvertere adresser i filen til koordinater (bruger Googles geocoding API).

Om programmet:

```
python csv2geodata.py --help
Usage: python csv2geodata.py [options] CSV-file

Options:
  -h, --help            show this help message and exit
  -l LOCATION_FIELD, --location-field=LOCATION_FIELD
                        Field in CSV-file containing a location that can be
                        geocoded, e.g. an address
  -o OUTPUT, --output=OUTPUT
                        Filename to write GeoJSON result to, default is
                        output.json
```

Brug programmet på CSV-filen:

```
python csv2geodata.py -l ADRESSE -o appleshops.json appleshops.txt
```

Kilde-kode til programmet:

```python
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
```