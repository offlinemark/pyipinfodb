# pyipinfodb.py

This is a simple python wrapper around [IPInfoDB](http://ipinfodb.com/)'s
free IP address geolocation [API](http://ipinfodb.com/ip_location_api.php).   
In order to use it, you need to get an [api key](http://ipinfodb.com/register.php).

*Note: This repo was originally forked from 
[here](https://github.com/sonicrules1234/pyipinfodb) but since that account
no longer seems to be active, I've taken things into my own hands 
and created a new repo for (relatively) active development of this API wrapper.*

## getting started

This wrapper is super easy to use.
If you just want to try it out: download this repo as a zip, unzip, and change to that directory in your terminal.
Then in a python interpreter: import it, instantiate an IPInfo object using your api key, and you're ready to go!
In this example, replace `<apikey>` with your api key.

    $ curl -L -O https://github.com/markmossberg/pyipinfodb/archive/master.zip
    $ unzip master.zip
    $ cd pyipinfodb-master
    $ python
    >>> import pyipinfodb
    >>> ip_lookup = pyipinfodb.IPInfo('<apikey>')
    >>> ip_lookup.get_country('8.8.8.8')
    {u'countryName': u'UNITED STATES', u'ipAddress': u'8.8.8.8', u'countryCode': u'US', u'statusMessage': u'', u'statusCode': u'OK'}

## installation

If you want to use this in a real project, you need to install the package.
You can use [pip](https://pypi.python.org/pypi/pip) to install the package straight from this github repo.

    $ pip install git+git://github.com/markmossberg/pyipinfodb.git

Or you can manually run the `setup.py` file in the zip file.

    $ python setup.py install

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

## contributing

Feel free to contribute! Just clone the repo using `git clone https://github.com/markmossberg/pyipinfodb.git` and install dependencies using `pip install -r requirements.txt`. I recommend using [virtualenv](http://www.virtualenv.org/) to create an isolated python environment for development.

### tests

Edit the `secrets.py.example` file and replace `<apikey>` with your key. Then rename the file to `secrets.py`. Now you can simply run tests with:

    $ nosetests
