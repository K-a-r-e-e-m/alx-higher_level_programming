#!/usr/bin/python3
'''Sends a request to URL and displays the value of X-Request-Id variable'''
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
