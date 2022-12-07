# Exer-01-Interacting-with-HTTP-Services-As-a-Client

from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

 # Encode the query string
 querystring = parse.urlencode(parms)

 # Make a GET request and read the response
 u = request.urlopen(url + '?' + querystring)
 resp = u.read()

 ###

from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

 # Encode the query string
 querystring = parse.urlencode(parms)

 # Make a POST request and read the response
 u = request.urlopen(url, querystring.encode('ascii'))
 resp = u.read()

###

from urllib import request, parse

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read()

###

import requests

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)


# Decoded text returned by the request
text = resp.text
