# Øvelse 1: simpel analyse

I denne øvelse vil vi lave et kort over verdens lande. [Kortet](http://cdb.io/120XA5v) viser hvor mange kilometer flod der er i et land. Lad som om det er mord, så det bliver lidt mere spændende.

![floder per lang](https://raw.github.com/skipperkongen/geodata-journalism/master/exercises/analytics/floder_per_land.png)

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

**Opgave 1**: Brug lige et øjeblik på at forstå hvad SQL'en gør.

Vælg "Map" tab, og indtast følgende under CSS menupunktet:

```css
/** choropleth visualization */

#world_borders{
  line-color: #FFF;
  line-opacity: 1;
  line-width: 1;
  polygon-opacity: 0.8;
}
#world_borders [ km_rivers <= 91914] {
   polygon-fill: #F03B20;
}
#world_borders [ km_rivers <= 48219] {
   polygon-fill: #FD8D3C;
}
#world_borders [ km_rivers <= 20767] {
   polygon-fill: #FECC5C;
}
#world_borders [ km_rivers <= 4120] {
   polygon-fill: #FFFFB2;
}
```

Klik på "Apply" og se på kortet.


## Spørgsmål

1. Hvordan talte du antal floder per land?
2. Hvad skete der med kortet efter du indtastede CSS?
