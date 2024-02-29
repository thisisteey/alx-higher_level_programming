#!/bin/bash
# Script that sends a request to a URL and displays only the status code of the response
curl -s -w "%{response_code}" -o /dev/null "$1"
