#!/usr/bin/python3
'''Takes in a letter and send a POST
request to http://0.0.0.0:5000/search_user
'''
from requests import post
from sys import argv


if __name__ == '__main__':

    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ''

    req = post('http://0.0.0.0:5000/search_user', data={"q": letter})

    try:
        json_req = req.json()
        if len(json_req) == 0:
            print('No result')  # If JSON is empty
        else:
            print(f'[{json_req.get("id")}] {json_req.get("name")}')
    except ValueError:
        print('Not a valid JSON')  # If JSON not valid
