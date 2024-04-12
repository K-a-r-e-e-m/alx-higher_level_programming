#!/bin/bash
# Displah Allow methods of http # Another solution ... | grep "Allow: " | cut -d " " -f 2- 
curl -is $1 | awk '/Allow: / { sub(/Allow: /, ""); print }' # substitute /Allow: / with empty string then print
