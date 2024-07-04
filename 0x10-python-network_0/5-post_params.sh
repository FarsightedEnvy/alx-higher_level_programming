#!/bin/bash
# Script that sends a POST request to a URL with parameters and displays the body of the response

# Usage: ./post_request.sh URL
# Example: ./post_request.sh http://localhost:5000/post

# Make sure exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Variables for POST data
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with parameters email and subject, display the body of the response
curl -s -X POST -d "email=$email" -d "subject=$subject" "$1"
