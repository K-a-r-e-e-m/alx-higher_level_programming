#!/usr/bin/python3
'''displays the value of the variable X-Request-Id in the response header'''
from requests import get
from sys import argv

if __name__ == '__main__':
    try:
        req = get(argv[1])
        print(req.headers['X-Request-Id'])
    except Exception as er:
        print(er)
