#!/bin/bash
# Script that sends a GET request to a URL and displays the body of the response for a 200 status code

# Usage: ./get_body.sh URL
# Example: ./get_body.sh http://localhost:5000

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Send a GET request to the URL and display the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read status_code
    if [[ $status_code -eq 200 ]]; then
        curl -s "$1"
    else
        echo "Error: Non-200 status code received ($status_code)"
    fi
}
