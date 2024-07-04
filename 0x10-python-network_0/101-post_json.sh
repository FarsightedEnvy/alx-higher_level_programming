#!/bin/bash
# Script that sends a JSON POST request to a URL and displays the body of the response

# Usage: ./json_post_request.sh URL JSON_FILE
# Example: ./json_post_request.sh http://localhost:5000/post data.json

# Make sure two arguments (URL and JSON file) are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

# Assign arguments to variables
url="$1"
json_file="$2"

# Check if JSON file exists
if [ ! -f "$json_file" ]; then
    echo "Error: JSON file '$json_file' not found."
    exit 1
fi

# Send a POST request with JSON data from file and display the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "@$json_file" "$url"
