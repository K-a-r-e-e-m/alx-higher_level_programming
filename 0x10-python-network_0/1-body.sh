#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -X GET -s -L $1 # -L that follow redirection until reach to final distenation in url
