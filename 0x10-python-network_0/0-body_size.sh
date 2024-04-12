#!/bin/bash
# Send a request to the given url and display size of body respose.
curl -s $1 | wc -c # -c count num of bytes
