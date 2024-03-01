#!/usr/bin/python3
"""
Script takes in a URL, sends a request & shows the X-Request-Id in the header
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        urlres = requests.get(urldt)
        if "X-Request-Id" in urlres.headers:
            print(urlres.headers["X-Request-Id"])
