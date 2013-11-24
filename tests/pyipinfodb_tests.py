from nose.tools import *
import pyipinfodb

key_file = open('api.key', 'r')
apikey = key_file.read()
apikey = apikey.replace('\n', '')
i = pyipinfodb.IPInfo(apikey)

def test_country():
    ideal = {
                u'countryName': u'UNITED STATES',
                u'ipAddress': u'155.33.148.202',
                u'countryCode': u'US',
                u'statusMessage': u'',
                u'statusCode': u'OK'
    }

    test = i.get_country('155.33.148.202')
    assert_equal(ideal, test)

def test_city():
    ideal = {u'countryCode': u'US', u'cityName': u'MOUNTAIN VIEW', u'zipCode': u'94043', u'longitude': u'-122.079', u'countryName': u'UNITED STATES', u'latitude': u'37.406', u'timeZone': u'-07:00', u'statusCode': u'OK', u'ipAddress': u'74.125.45.100', u'statusMessage': u'', u'regionName': u'CALIFORNIA'}

    test = i.get_city('74.125.45.100')
    assert_equal(ideal, test)

def test_city_noParam():
    ideal = {u'countryCode': u'US', u'cityName': u'BOSTON', u'zipCode': u'02115', u'longitude': u'-71.0968', u'countryName': u'UNITED STATES', u'latitude': u'42.3419', u'timeZone': u'-04:00', u'statusCode': u'OK', u'ipAddress': u'155.33.148.202', u'statusMessage': u'', u'regionName': u'MASSACHUSETTS'}

    test = i.get_city()
    assert_equal(ideal, test)

