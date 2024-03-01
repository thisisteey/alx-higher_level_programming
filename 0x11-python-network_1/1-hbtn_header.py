#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and displays the X-Request-Id
"""
import urllib.request as urlreq
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        with urlreq.urlopen(urldt) as urlres:
            print(urlres.headers["X-Request-Id"])
