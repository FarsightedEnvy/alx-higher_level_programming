#!/bin/bash
# Script that sends a request to a URL and displays only the status code of the response

# Usage: ./status_code.sh URL
# Example: ./status_code.sh http://localhost:5000

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Send a HEAD request to the URL and extract the status code
curl -s -I "$1" | grep HTTP | awk '{print $2}' | tail -n 1
