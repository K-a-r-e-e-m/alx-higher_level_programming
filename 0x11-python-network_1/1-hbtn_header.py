#!/usr/bin/python3
'''Sends a request to URL and displays the value of X-Request-Id variable'''
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
