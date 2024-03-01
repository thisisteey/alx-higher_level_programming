#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        urldt = sys.argv[1]
        email = sys.argv[2]
        encdt = [("email", email)]
        urlres = requests.post(urldt, data=encdt)
        print(urlres.text)
