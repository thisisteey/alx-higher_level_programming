#!/usr/bin/python3
"""
Script that takes in a URL, sends a request & shows the answer decoded in utf-8
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        urldt = sys.argv[1]
        try:
            with request.urlopen(urldt) as urlres:
                print(urlres.read().decode("utf-8"))
        except error.HTTPError as httpex:
            print(f"Error code: {httpex.code}")
