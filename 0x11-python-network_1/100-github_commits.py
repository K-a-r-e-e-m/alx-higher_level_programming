#!/usr/bin/python3
'''Get GitHub credentials (username and password)
   and uses the GitHub API to display your id
'''
from requests import get
from sys import argv

if __name__ == '__main__':

    req = get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits')
    json_data = req.json()

    try:
        for i in range(10):
            sha = json_data[i].get('sha')
            author_name = json_data[i].get('commit').get('author').get('name')

            print(f'{sha}: {author_name}')

    except IndexError:
        pass
