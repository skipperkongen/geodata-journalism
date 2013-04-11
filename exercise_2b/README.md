# Konvertering mellem formater

Brug ogr2ogr til at lave følgende konverteringer

1. konverter kommune_4326.shp til kommune.json
2. importer kommune.json i PostgreSQL

## Hints

* [ogr2ogr cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet), "Convert between vector formats"
* Slå PostGIS til på en database: `create extension postgis;`