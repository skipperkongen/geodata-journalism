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