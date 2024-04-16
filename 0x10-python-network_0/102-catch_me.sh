#!/bin/bash
# Responds from server with a message "You got me!".
curl -sd "You got me!" 0.0.0.0:5000/catch_me
