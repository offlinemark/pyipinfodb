from nose.tools import *
import pyipinfodb
import secrets

apikey = secrets.apikey
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
    ideal = {u'cityName': u'MOUNTAIN VIEW',
         u'countryCode': u'US',
         u'countryName': u'UNITED STATES',
         u'ipAddress': u'8.8.8.8',
         u'latitude': u'37.406',
         u'longitude': u'-122.079',
         u'regionName': u'CALIFORNIA',
         u'statusCode': u'OK',
         u'statusMessage': u'',
         u'timeZone': u'-08:00',
         u'zipCode': u'94043'
    }
    test = i.get_city('8.8.8.8')
    assert_equal(ideal, test)
