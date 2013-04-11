# Øvelse 2: Projektioner

## 1: Download data: 

Download data fra CartoDB:

```
curl -o ekstrabladet_4326.json 'https://skipperkongen.cartodb.com/api/v2/sql?format=GeoJSON&q=select+*+FROM+generisk_geodata+WHERE+name=%27Ekstrabladet%27'
```

## 2: Se på data

* Åben fil ekstrabladet.json i en teksteditor (brug eventuelt http://jsonformatter.curiousconcept.com/ til at formatere indholdet pænt)
* Bid mærke i koordinaterne

## 3: Skift projektion

Brug `ogr2ogr` til at transformere koordinaterne fra Lat/Long til Google projektion:

```
ogr2ogr -f "GeoJSON" ekstrabladet_3758.json -s_srs "EPSG:4326" -t_srs "EPSG:3857" ekstrabladet_4326.json 
```