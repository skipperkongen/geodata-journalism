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

**Opgave 2**: Brug lige et øjeblik på at forstå hvad ovenstående CSS gjorde. 

Det du indtastede er en variant af CSS der hedder CartoCSS. Det kan bruges til at style geodata i et kort på forskellige måder.

# Øvelse 2: Spatial joins

Spatial joins i SQL er en vigtig måde at analysere data på. Du kan f.eks. joine to tabeller R og S på følgende måder:

* **Intersects**: Kombinér rækker fra R med rækker fra S hvor de overlapper hinanden
* **Distance**: Kombinér rækker fra R med rækker fra S, som er indenfor en vis afstand

Vi kan bruge de to tabeller fra før, *rivers* og *world_borders*.

Intersects join (lande sammenstillet med floder der løber igennem landet):

```sql
SELECT R.name1, S.name 
FROM rivers AS R 
JOIN world_borders AS S 
ON ST_Intersects(r.the_geom, S.the_geom)
```

Distance join (lande i Afrika som er indenfor en afstand af 500km fra Niger floden):

```sql
SELECT distinct S.name
FROM rivers AS R 
JOIN world_borders AS S 
ON ST_DWithin(st_transform(st_setsrid(R.the_geom, 4326), 3857), st_transform(st_setsrid(S.the_geom, 4326), 3857), 500000)
WHERE R.name1='Niger' and S.region=2
```

Hvis ovenstående distance join skal visualiseres i CartoDB, skal man vælge alle kolonnerne fra S.

```sql
SELECT distinct S.*
FROM rivers AS R 
JOIN world_borders AS S 
ON ST_DWithin(st_transform(st_setsrid(R.the_geom, 4326), 3857), st_transform(st_setsrid(S.the_geom, 4326), 3857), 500000)
WHERE R.name1='Niger' and S.region=2
```


