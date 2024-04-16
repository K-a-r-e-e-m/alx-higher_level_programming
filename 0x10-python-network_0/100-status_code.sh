#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response
curl -s --output /dev/null --write-out "%{http_code}" $1 ; echo ""
