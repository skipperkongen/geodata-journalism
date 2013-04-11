# Konvertering mellem formater

Brug ogr2ogr til at lave følgende konverteringer

1. konverter kommune_4326.shp til kommune.json
2. importer kommune.json i PostgreSQL
3. exporter kommuner i øst-danmark fra PostgreSQL til GeoJSON

## Hints

ogr2ogr cheat sheet: https://github.com/dwtkns/gdal-cheat-sheet, søg på "Convert between vector formats"

Slå PostGIS til på en database:

```sql
create extension postgis;
```

ogr2ogr har en -sql option hvor man kan vælge de rækker der skal exporteres:

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
