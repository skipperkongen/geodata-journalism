# Løsninger til 2b

1. ogr2ogr -f "GeoJSON" kommuner_4326.json exercise_2/data/kommune_4326.shp
2. ogr2ogr -f "PostgreSQL" PG:"host=localhost user=postgres password=postgres dbname=learning" kommuner_4326.json
3. ogr2ogr ostdanmark.shp PG:"host=localhost user=postgres password=postgres dbname=learning" -sql "select * from kommuner where wkb_geometry && ST_SetSRID('BOX(11 54, 16 58)'::box2d, 4326)"


Bounding box til 3. fundet med "select st_extent(wkb_geometry) from kommuner;"
