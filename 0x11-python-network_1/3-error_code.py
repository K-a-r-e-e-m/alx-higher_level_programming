#!/usr/bin/python3
'''Displays the body of the response (decoded in utf-8)'''
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode())
    except HTTPError as er:
        print(f'Error code: {er.status}')
