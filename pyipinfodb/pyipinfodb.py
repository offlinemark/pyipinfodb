#!/usr/bin/env python

"""
    Simple python wrapper around the IPInfoDB API.
"""

import json
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
import socket

class IPInfo() :
    def __init__(self, apikey):
        self.apikey = apikey

    def get_ip_info(self, baseurl, ip=None):
        """
            Same as get_city and get_country, but a baseurl is required.
            This is for if you want to use a different server that uses
            the php scripts on ipinfodb.com.
        """

        passdict = {'format': 'json', 'key': self.apikey}
        if ip:
            try:
                # allows user to enter in domain instead of ip
                passdict['ip'] = socket.gethostbyaddr(ip)[2][0]
            except socket.herror:
                # if domain is not found, just use input
                passdict['ip'] = ip
        url = baseurl + "?" + urlencode(passdict)
        urlobj = urllib2.urlopen(url)
        data = urlobj.read()
        urlobj.close()
        datadict = json.loads(data.decode('utf-8'))
        return datadict

    def get_country(self, ip=None):
        """
            Gets the location with the context of the country of the given IP.
            If no IP is given, then the location of the client is given.
            The timezone option defaults to False, to spare the server some queries.
        """

        baseurl = 'http://api.ipinfodb.com/v3/ip-country/'
        return self.get_ip_info(baseurl, ip)

    def get_city(self, ip=None):
        """
            Gets the location with the context of the city of the given IP.
            If no IP is given, then the location of the client is given.
            The timezone option defaults to False, to spare the server some queries.
        """

        baseurl = 'http://api.ipinfodb.com/v3/ip-city/'
        return self.get_ip_info(baseurl, ip)
