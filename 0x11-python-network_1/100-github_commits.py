#!/usr/bin/python3
'''Get GitHub credentials (username and password)
   and uses the GitHub API to display your id
'''
from requests import get
# from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    # We also can user auth=HTTPBasicAuth(...) but remove it is shorhand
    req = get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits')
    json_data = req.json()
    for i in range(10):
        print(f'{json_data[i].get("sha")}: \
              {json_data[i].get("commit").get("author").get("name")}')
