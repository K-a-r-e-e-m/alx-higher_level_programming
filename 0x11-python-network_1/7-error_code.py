#!/usr/bin/python3
'''Sends a request and handle errors'''
from requests import get, HTTPError
from sys import argv


if __name__ == '__main__':
    req = get(argv[1])
    if req.status_code >= 400:
        print(f'Error code: {req.status_code}')
    else:
        print(req.text)
            
