# Øvelse 2: Projektioner

I denne øvelse vil vi transformere data fra en projektion til en anden. Hvorfor gør vi det? Data gøres tilgængelig i alle mulige forskellige projektioner (det offentlige Danmark deler typisk data i den "danske" projektion EPSG:25832). Nogle systemer håndterer kun nogle af  disse, så der kan opstå problemer ved import hvis data ikke reprojiceres først.

Følgende angiver samme sted på jorden (Rådhuspladsen):

```python
(724349.775302884, 6175905.3508779) # Den danske stat
(1399102.1714033, 7494384.2880911) # Google
(12.5683486461639, 55.6770097095364) # Longitude/Latitude
```

## Del 1: Opvarmning

Reprojektion af en enkelt punkt-feature (placeringen af Ekstrabladet)

### 1: Download data: 

Download Ekstrabladets placering fra CartoDB:

```
curl -o ekstrabladet_4326.json 'https://skipperkongen.cartodb.com/api/v2/sql?format=GeoJSON&q=select+*+FROM+generisk_geodata+WHERE+name=%27Ekstrabladet%27'
```

### 2: Se på data

* Kig på data i filen ekstrabladet_4326_.json (formattet er GeoJSON)
* Bid mærke i koordinaterne

**Hint**: `cat ekstrabladet_4326.json | python -mjson.tool`

### 3: Skift projektion

Brug `ogr2ogr` til at transformere koordinaterne fra Lat/Long til Google projektion:

```
ogr2ogr -f "GeoJSON" ekstrabladet_3857.json -s_srs "EPSG:4326" -t_srs "EPSG:3857" ekstrabladet_4326.json 
```

Sammenlign indholdet af de to filer:

```
cat ekstrabladet_4326.json | python -mjson.tool; cat ekstrabladet_3857.json | python -mjson.tool
```

## Del 2: Transformation af et helt datasæt

Importer offentlige danske data ind i CartoDB.

### 4: Reprojicer danske kommuner

Data fra det offentlige Danmark er typisk i projektionen EPSG:25832, f.eks. datasættet [DAGI](http://download.kortforsyningen.dk/content/danmarks-administrative-geografiske-inddeling-1500000) (Danmarks Administrative Geografiske Inddeling). CartoDB fejler hvis man prøver på at importere data i denne projektion (burde den nok ikke, men det gør den).

Derfor vil vi reprojicere til latitude/longitude først.

```
cd data
unzip kommune_25832.zip
ogr2ogr kommune_4326.shp -t_srs "EPSG:4326" kommune_25832.shp
zip kommune_4326.zip kommune_4326.*
```

### 5: Upload til CartoDB

Brug upload-formularen ("Create new Table") i CartoDB dashboard til at importere zip fil med kommuner.

### 6: Åben table og se på kort

Hvis du er zoomet helt ud, så zoom ind på Danmark.