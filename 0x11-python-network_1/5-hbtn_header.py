#!/usr/bin/python3
'''displays the value of the variable X-Request-Id in the response header'''
from requests import get
from sys import argv


req = get(argv[1])
print(req.headers['X-Request-Id'])
