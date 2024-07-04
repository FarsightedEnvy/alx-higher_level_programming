#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me to get the server to respond with "You got me!"

# Usage: ./catch_me.sh
# Example: ./catch_me.sh

# Send a PUT request with a specific header to cause the server to respond with "You got me!"
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
