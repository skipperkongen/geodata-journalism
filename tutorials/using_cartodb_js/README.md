# cartdb.js tutorials

## Tutorial 1

First download [zip file with examples](curl -o examples.zip https://raw.github.com/Vizzuality/CartoDB-Tutorials/master/cartodb-js/data/examples.zip), next open up the [create a map](https://github.com/Vizzuality/CartoDB-Tutorials/blob/master/cartodb-js/create_a_map.md) page in a browser.

This tutorial will teach you:

* How to create a CartoDB driven map on your web site
* How to share a CartoDB table, so that you can show the data in your new map
* How to pass SQL from Javascript to CartoDB, to filter the data dynamically!
* Add base layers to the map, e.g. OpenStreetMap

Notice that the map-box tile url in the tutorial didn't work. I replaced with this one taken from my [list of free tiles](http://skipperkongen.dk/2012/10/18/free-map-tiles/):

```javascript
L.tileLayer('http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.jpg', {
				attribution: 'Stamen',
				subdomains: ['a', 'b', 'c', 'd']
}).addTo(map);
```

My final map:

```javascript
<html>
<head>
  <link rel="stylesheet" href="http://libs.cartocdn.com/cartodb.js/v2/themes/css/cartodb.css" />
	<script src="http://libs.cartocdn.com/cartodb.js/v2/cartodb.js"></script>
	<style>
	html, body {padding: 0; margin: 0;}
	#cartodb-map { width: 100%; height:100%; background: black;}
	</style>
	<script>
  var map;
  function init(){
	// initiate leaflet map
	map = new L.Map('cartodb-map', { 
	  center: [0,0],
	  zoom: 2
	})

	L.tileLayer('http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.jpg', {
					attribution: 'Stamen',
					subdomains: ['a', 'b', 'c', 'd']
	}).addTo(map);

	var layerUrl = 'http://skipperkongen.cartodb.com/api/v1/viz/14255/viz.json'

	var layerOptions = {
		query: "SELECT * FROM {{table_name}} where adm0_a3 = 'USA'",
		tile_style: "#{{table_name}}{marker-fill: red; marker-width: 14; marker-line-color: white; marker-line-width: 3;}"
	}

	cartodb.createLayer(map, layerUrl, layerOptions)
	 .on('done', function(layer) {
	  map.addLayer(layer);
	}).on('error', function() {
	  //log the error
	});

  }
	</script>
</head>
<body onload="init()">
  <div id='cartodb-map'></div>
</body>
</html>
```

## Tutorial 2

Follow up with these:

* https://github.com/Vizzuality/CartoDB-Tutorials/blob/master/cartodb-js/query_by_distance.md
* https://github.com/Vizzuality/CartoDB-Tutorials/blob/master/cartodb-js/toggle_map_view.md
* https://github.com/Vizzuality/CartoDB-Tutorials/blob/master/cartodb-js/basic_data_queries.md
* https://github.com/Vizzuality/CartoDB-Tutorials/blob/master/cartodb-js/adding_infowindows.md
* https://github.com/Vizzuality/CartoDB-Tutorials/blob/master/cartodb-js/two_layers.md