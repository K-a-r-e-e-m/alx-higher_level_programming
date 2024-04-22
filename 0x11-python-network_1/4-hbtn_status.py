#!/usr/bin/python3
'''This module uses a requests package to fetch url'''
import requests
req = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f'\t- type: {type(req.text)}')
print(f'\t- content: {req.text}')
