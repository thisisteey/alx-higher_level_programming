#!/bin/bash
# Script that takes in a URL as an argument, sends a GET, and displays the body of the response
curl -sL -H "X-School-User-Id: 98" "$1"
