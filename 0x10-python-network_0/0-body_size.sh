#!/bin/bash
# Script that sends a request to a URL and displays the size of the response body

# Usage: ./body_size.sh URL
# Example: ./body_size.sh http://localhost:5000

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Retrieve the size of the response body using curl in silent mode
SIZE=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')

# Display the size in bytes
echo "Size of the body: $SIZE bytes"
