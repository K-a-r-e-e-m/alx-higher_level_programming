#!/usr/bin/python3
'''Get GitHub credentials (username and password)
   and uses the GitHub API to display your id
'''
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    req = get('https://api.github.com', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
