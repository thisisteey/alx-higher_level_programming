#!/usr/bin/python3
"""
Script that takes in a URL, sends a request & shows the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        urlres = requests.get(urldt)
        urlstatus = urlres.status_code
        if urlstatus >= 400:
            print(f"Error code: {urlstatus}")
        else:
            print(urlres.text)
