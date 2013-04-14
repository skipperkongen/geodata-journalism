# Konvertering mellem formater

Brug ogr2ogr til at lave følgende konverteringer

1. konverter kommune_4326.shp til kommune.json (ligger i data mappen)
2. importer kommune.json i PostgreSQL
3. eksporter kommuner i øst-danmark fra PostgreSQL til en shape fil

Du kan prøve selv med de hints der står herunder, eller hoppe direkte til [løsningerne](https://github.com/skipperkongen/geodata-journalism/blob/master/exercises/converting/solutions.md). 

## Hints

**Opgave 1**

ogr2ogr cheat sheet: https://github.com/dwtkns/gdal-cheat-sheet, søg på "Convert between vector formats"

**Opgave 2**

Slå PostGIS til på en database:

```sql
create extension postgis;
```

**Opgave 3**

ogr2ogr har en -sql option hvor man kan vælge de rækker der skal eksporteres:

```
ogr2ogr -f "GeoJSON" output.geojson \
PG:"host=localhost user=foo password=bar dbname=osm" \
-sql "select foo from bar where baz='xxx'" \
-t_srs "epsg:3189"
```

PostGIS bounding box query:

```sql
SELECT * FROM TABLE 
WHERE the_geom && ST_SetSRID(
    'BOX(903377.0 7283641.0,1691764.0 7914275.0)'::box2d, 
    3857
)
```

Beregn bounding box for alle rækker i en tabel:

```sql
SELECT ST_Extent(the_geom) FROM TABLE;
```
