# Fra [stuff] til geodata

## Øvelse: Geokodning af adresser

**Problem**: Lad os sige at vi har fundet en tekst-fil (CSV) med adresser på noget vigtigt (Apple-shops nær København). Vi vil gerne lave en geodata ud af filen, så vi kan vise informationen på et kort, og vi har valgt GeoJSON som vores output format:

Data i [CSV-fil](https://raw.github.com/skipperkongen/geodata-journalism/master/exercises/geocoding/appleshops.txt):

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

Jeg har skrevet et Python program som kan geokode adresser i en CSV-fil (geokode = omdanne tekst til koordinater). [Kildekoden til programmet](https://github.com/skipperkongen/geodata-journalism/blob/master/exercises/geocoding/csv2geodata.py) findes i dette repository (og står også længere nede på siden).

Du kan få usage for programmet ved at kalde:

```
python csv2geodata.py --help
```

**Opgave 1**:
Kald [programmet]((https://github.com/skipperkongen/geodata-journalism/blob/master/exercises/geocoding/csv2geodata.py)) med [CSV-filen](https://raw.github.com/skipperkongen/geodata-journalism/master/exercises/geocoding/appleshops.txt) som input, og få en GeoJSON fil ud af det:


**Løsning 1**: 

```
python csv2geodata.py -l ADRESSE -o appleshops.json appleshops.txt
```

**Opgave 2**: Vis indholdet af GeoJSON filen på et kort i browseren. Til formålet bruger vi javascript biblioteket Leaflet.

**Løsning 2**: Hvis du har oprettet GeoJSON filen (output.json), kan du åbne [map.html] side i en browser (HTML-filen skal ligge i samme directory som JSON filen). Den bør vise et kort med dine adresser.



## Bilag

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