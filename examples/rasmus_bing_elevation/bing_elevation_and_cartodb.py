#!/usr/bin/python
# -*- coding: utf-8 -*-

from cartodb import CartoDBAPIKey, CartoDBException
import simplejson as json
import urllib
import sys

def getElevationSamples(identifier):
  
  elevation_base_url = "http://dev.virtualearth.net/REST/v1/Elevation/Polyline"
  bingmaps_api_key   = '' # NEEDED
  bingmaps_url       = elevation_base_url + "?key=" + bingmaps_api_key
  cartodb_api_key    = '' # NEEDED
  cartodb_domain     = 'frederiksen'
  table              = 'tourdefrance2013stages'
  identifierColumn   = 'stage_number'
  samplesColumn      = 'height_samples'
  cl                 = CartoDBAPIKey(cartodb_api_key, cartodb_domain)

  try:

    ########## CALCULATE NUMBER OF SAMPLES ##########

    sql        = "SELECT length FROM %s WHERE %s = %s" % (table, identifierColumn, identifier)
    length     = cl.sql(sql)
    length     = float(length['rows'][0]['length'])
    numSamples = int(round(length/250.0))
    # Bing Maps API can only return a maximum of 1024 samples
    numSamples = 1024 if numSamples > 1024 else numSamples

    ########## GET ALL THE WAYPOINTS FROM CARTODB ##########

    print "Acessing route information from %s = %s in %s at %s.cartodb.com ..." % (identifierColumn, identifier, table, cartodb_domain)

    sql = """SELECT
      st_asgeojson(
        st_transform(
          st_linemerge(the_geom),
          4326
        )
      )
      FROM %s
      WHERE stage_number = %s;
    """ % (table, identifier)
    stageRoute = cl.sql(sql)

    # Extract the coordinates array from the response
    coordinates = json.loads(stageRoute['rows'][0]['st_asgeojson'])['coordinates']

    ########## QUERY THE BING MAPS API ##########

    # Create a string of coordinates on the form: lat,lon|lat,lon| ... |lat,lon
    # as per the Bing Maps API
    coordinates = ",".join(str(point[1])+","+str(point[0]) for point in coordinates)

    # Create the POST data that Bing Maps API expects
    args = {
      'points'  : coordinates,
      'heights' : 'sealevel', # alternatively 'ellipsoid'
      'samples' : numSamples
    }

    print "Querying Microsoft Bing Elevation API for " + str(numSamples) + " samples along the route..."
    rawResponse = urllib.urlopen(bingmaps_url, urllib.urlencode(args))
    response = json.load(rawResponse)['resourceSets'][0]['resources'][0]['elevations']

    ########## SAVE RESULT BACK ##########

    print "Updating height samples for stage %s in %s at %s.cartodb.com ..." % (identifier, table, cartodb_domain)

    sql = "UPDATE %s SET %s = \'%s\' WHERE %s = %s" % (table, samplesColumn, str(response), identifierColumn, identifier))
    cl.sql(sql)

    print "Done"

  except CartoDBException as e:
    print ("some error ocurred", e)

if __name__ == '__main__':
  getElevationSamples(sys.argv[1])