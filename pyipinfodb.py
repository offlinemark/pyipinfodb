import json, urllib, urllib2

def GetIPInfo(baseurl, ip=None, timezone=False) :
    """Same as GetCity and GetCountry, but a baseurl is required.  This is for if you want to use a different server that uses the the php scripts on ipinfodb.com."""
    passdict = {"output":"json"}
    if ip :
        passdict["ip"] = ip
    if timezone :
        passdict["timezone"] = "true"
    else :
        passdict["timezone"] = "false"
    urldata = urllib.urlencode(passdict)
    url = baseurl + "?" + urldata
    urlobj = urllib2.urlopen(url)
    data = urlobj.read()
    urlobj.close()
    datadict = json.loads(data)
    return datadict

def GetCity(ip=None, timezone=False) :
    """Gets the location with the context of the city of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
    baseurl = "http://ipinfodb.com/ip_query.php"
    return GetIPInfo(baseurl, ip, timezone)

def GetCountry(ip=None, timezone=False) :
    """Gets the location with the context of the country of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
    baseurl = "http://ipinfodb.com/ip_query_country.php"
    return GetIPInfo(baseurl, ip, timezone)
