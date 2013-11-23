# pyipinfodb.py

This is a simple python wrapper around the [IPInfoDB](http://ipinfodb.com/) [API](http://ipinfodb.com/ip_location_api.php)
which is a free IP geolocation API.  
In order to use it, you need to get an [api key](http://ipinfodb.com/register.php).

## getting started

This wrapper is super easy to use. If you just want to try it out: download this repo as a zip, unzip, and in change to 
that directory in your terminal.
Then in a python interpreter: import it, instantiate an IPInfo object using your api key, and you're ready to go!
In this example, replace `<apikey>` with your api key.

    $ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyipinfodb
    >>> ip_lookup = pyipinfodb.IPInfo('<apikey>')
    >>> ip_lookup.get_country('74.125.45.100')
    {u'countryName': u'UNITED STATES', u'ipAddress': u'74.125.45.100', u'countryCode': u'US', u'statusMessage': u'', u'statusCode': u'OK'}

## installation

If you want to use this in a real project, you need to install the package.
The recommended way to do this is to first use [virtualenv](https://pypi.python.org/pypi/virtualenv) to create an
isolated Python environment so you don't mess up your system environment. Then you can use [pip](https://pypi.python.org/pypi/pip)
to install the package straight from this github repo.

    $ mkdir awesome_project
    $ cd awesome_project
    $ virtualenv venv
    $ . venv/bin/activate
    (venv)$ pip install git+git://github.com/markmossberg/pyipinfodb.git
    (venv)$ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pyipinfodb
    >>>
    (venv)$ deactivate
    $

## documentation

#### `get_country(self, ip=None)`

Return a dictionary with country information based on ip address passed as parameter.  
Example output:

    {u'countryName': u'UNITED STATES', u'ipAddress': u'74.125.45.100', u'countryCode': u'US', u'statusMessage': u'', u'statusCode': u'OK'}

If no parameters are passed, returns information about the client ip making the request.

#### `get_city(self, ip=None)`

Return a dictionary with detailed country, city, and timezone information based on ip address passed as parameter.  
Example output:

    {u'countryCode': u'US', u'cityName': u'MOUNTAIN VIEW', u'zipCode': u'94043', u'longitude': u'-122.079', u'countryName': u'UNITED STATES', u'latitude': u'37.406', u'timeZone': u'-07:00', u'statusCode': u'OK', u'ipAddress': u'74.125.45.100', u'statusMessage': u'', u'regionName': u'CALIFORNIA'}

If no parameters are passed, returns information about the client ip making the request.

Avoid using this function if you don't need this level of detail, it helps keep the load lower on IPInfoDB's servers :)

#### `get_ip_info(self, baseurl, ip=None)`

This is the backend that powers the above functions. It lets you specify a base url to use for your requests. You probably won't need to use this function.

