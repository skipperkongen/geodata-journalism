# Importing data into CartoDB

CartoDB can import ZIP, KML, CSV, GPX, XLS.

## Recipe to import CSV data with X,Y into CartoDB

Snippet of data `cities_dk.csv`:

```csv
"x","y","srid","name","place","population"
1128407,7847260,3857,"Ugilt","hamlet",-1
1041789,7411187,3857,"Styding","hamlet",-1
1064576,7424619,3857,"Fjelstrup","hamlet",-1
...
```

1. Use CartoDB interface to import CSV file. This creates a table with string columns
2. Create a view:
```sql
SELECT 
	ST_SetSrid(ST_MakePoint(x::float, y::float), 3857) as point_webmercator, 
	name, 
	place, 
	population
FROM 
	cities_dk
```

