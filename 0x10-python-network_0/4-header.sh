#!/bin/bash
# Script that sends a GET request to a URL with a custom header and displays the body of the response

# Usage: ./custom_header_request.sh URL
# Example: ./custom_header_request.sh http://localhost:5000

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Send a GET request to the URL with custom header X-School-User-Id: 98 and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
