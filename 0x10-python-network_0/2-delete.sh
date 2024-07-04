#!/bin/bash
# Script that sends a DELETE request to a URL and displays the body of the response

# Usage: ./delete_request.sh URL
# Example: ./delete_request.sh http://localhost:5000/delete

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Send a DELETE request to the URL and display the body of the response
curl -s -X DELETE "$1"
