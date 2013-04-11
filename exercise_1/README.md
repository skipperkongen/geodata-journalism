# Øvelse 1: simpel analyse

## Forbered data

1. Log ind på CartoDB
2. Opret to tabeller via "common data" menuen:
    * Opret en “world borders” tabel
    * Opret en “rivers” tabel

## Arbejd med data

**Tænk**: Hvordan ville du skrive et SQL query, der for hvert land opgør hvor mange floder der løber igennem landet?

**En løsning**

Vælg world border tabellen. Klik på SQL og indtast følgende:

```sql
SELECT
	b.*,
	(SELECT count(*) FROM rivers r where st_intersects(r.the_geom,b.the_geom)) AS num_rivers 
FROM world_borders b
```

Vælg "Map" tab, og under CSS menu indtaster du følgende:

```css
#world_borders{
 line-color: #FFF;
 line-opacity: 1;
 line-width: 1;
 polygon-opacity: 0.8;
}
#world_borders [ num_rivers <= 218.0] {
  polygon-fill: #B10026;
}
#world_borders [ num_rivers <= 54.0] {
  polygon-fill: #E31A1C;
}
#world_borders [ num_rivers <= 22.0] {
  polygon-fill: #FC4E2A;
}
#world_borders [ num_rivers <= 17.0] {
  polygon-fill: #FD8D3C;
}
#world_borders [ num_rivers <= 13.0] {
  polygon-fill: #FEB24C;
}
#world_borders [ num_rivers <= 9.0] {
  polygon-fill: #FED976;
}
#world_borders [ num_rivers <= 4.0] {
  polygon-fill: #FFFFB2;
}
```

## Spørgsmål

1. Hvordan blev `num_rivers` kolonnen skabt?
2. Hvad gør den CSS du indtastede?
