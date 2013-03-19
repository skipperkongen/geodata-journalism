from geopy import geocoders
import httplib
import urllib2, urllib
import sys
import pdb
import random

def main(options, args):

	print "Geocoding", options.location	
	# Using geocoders: https://code.google.com/p/geopy/wiki/GettingStarted
	g = geocoders.GoogleV3()
	for place, (lat, lng) in g.geocode( options.location, exactly_one=False ):
		print "%s: %.5f, %.5f" % (place, lat, lng)
	
	lat += (random.random() - 0.5) * 0.01
	lng += (random.random() - 0.5) * 0.01
	
	print "Pushing message to CartoDB observations"
	conn = httplib.HTTPSConnection("ebtutorial.cartodb.com")
	obs_id, msg, api_key = options.observer_id, " ".join(args), options.api_key
	sql = \
		"INSERT INTO observations(the_geom, observer_id, message) \
		VALUES (ST_GeomFromText('POINT(%.5f %.5f)',%d),'%s','%s')" \
		% (lng, lat, 4326, obs_id, msg)

	print sql
	path = "/api/v2/sql?q=%s&api_key=%s" % (urllib.quote_plus(sql), api_key)
	#sys.exit(0)
			
	conn.request("GET", path)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	print data
	
if __name__ == '__main__':
	from optparse import OptionParser
	usage = "usage: %prog [options] message"
	parser = OptionParser(usage=usage)
	parser.add_option("-l", "--location", dest="location",
	                  help="location to geocode")
	parser.add_option("-a", "--api-key", dest="api_key",
	                  help="CartoDB api key")
	parser.add_option("-i", "--observer-id", dest="observer_id",
	                  help="CartoDB api key")
	(options, args) = parser.parse_args()
	
	main(options, args)