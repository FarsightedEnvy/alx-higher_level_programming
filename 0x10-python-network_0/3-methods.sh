#!/bin/bash
# Script to display all HTTP methods accepted by a server for a given URL

# Usage: ./supported_methods.sh URL
# Example: ./supported_methods.sh http://localhost:5000

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Send an OPTIONS request to the URL and display supported methods
curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
