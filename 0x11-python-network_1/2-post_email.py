#!/usr/bin/python3
'''Sends POST request to URL with email as a parameters and displays body'''
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':

    variable = {'email': sys.argv[2]}  # String data

    data = urllib.parse.urlencode(variable)  # Encoding data
    data = data.encode('utf-8')  # Specify encoding to bytes with utf-8
    req = urllib.request.Request(sys.argv[1], data, variable)  # Send a request
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode())  # Decode the body of response from bytes to string
