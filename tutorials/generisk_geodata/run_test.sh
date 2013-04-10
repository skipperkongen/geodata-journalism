#!/bin/sh
curl 'https://skipperkongen.cartodb.com/api/v2/sql?q=DELETE++FROM+generisk_geodata+WHERE+1=1&api_key=d46d9993632140e8ae3fad653489327baf7f5b5e'
python push_generic.py --location 'Rådhuspladsen 37, 1785 København' --name 'Ekstrabladet' --description 'Dagblad' --api-key d46d9993632140e8ae3fad653489327baf7f5b5e
python push_generic.py --location 'Universitetsparken 5, 2100 København Ø' --name 'DIKU' --description 'Institut' --api-key d46d9993632140e8ae3fad653489327baf7f5b5e
python push_generic.py --location 'Rentemestervej 8, 2200 København NV' --name 'GST' --description 'Styrelse' --api-key d46d9993632140e8ae3fad653489327baf7f5b5e


# Se kort: http://cdb.io/XngAqa