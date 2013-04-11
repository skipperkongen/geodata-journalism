# Øvelse 1: simpel analyse

I denne øvelse vil vi lave et kort over verdens lande. [Kortet](http://cdb.io/120XA5v) viser hvor mange kilometer flod der er i et land. Lad som om det er mord, så det bliver lidt mere spændende.

![floder per lang](https://raw.github.com/skipperkongen/geodata-journalism/master/exercise_3/floder_per_land.png)

## Opret Kort

Log ind på CartoDB

Opret to tabeller via "common data" menuen:

1. “world borders”
2. “rivers”

Skift navne så tabellerne hedder "world_borders" og "rivers")

Vælg "world_border" tabellen

Klik på SQL (se til højre under "Table" tab) og indtast følgende:

```sql
SELECT 
	b.*,
	(SELECT sum(ST_Length(ST_Transform(
         the_geom,
		 3857)) /1000.0) 
	 FROM 
	     rivers r
	 WHERE
	     st_intersects(
	         r.the_geom,
	         b.the_geom))
	AS km_rivers
FROM world_borders b
```

Vælg "Map" tab, og under CSS menu indtaster du følgende:

```css
/** choropleth visualization */

#world_borders{
  line-color: #FFF;
  line-opacity: 1;
  line-width: 1;
  polygon-opacity: 0.8;
}
#world_borders [ km_rivers <= 91913.7015549117] {
   polygon-fill: #B10026;
}
#world_borders [ km_rivers <= 3772.51105107822] {
   polygon-fill: #E31A1C;
}
#world_borders [ km_rivers <= 2579.03674063611] {
   polygon-fill: #FC4E2A;
}
#world_borders [ km_rivers <= 1831.83830679438] {
   polygon-fill: #FD8D3C;
}
#world_borders [ km_rivers <= 1186.54901880401] {
   polygon-fill: #FEB24C;
}
#world_borders [ km_rivers <= 711.278107065951] {
   polygon-fill: #FED976;
}
#world_borders [ km_rivers <= 357.937058658957] {
   polygon-fill: #FFFFB2;
}
```

Klik på "Apply" og se på kortet.


## Spørgsmål

1. Hvordan talte du antal floder per land?
2. Hvad skete der med kortet efter du indtastede CSS?
