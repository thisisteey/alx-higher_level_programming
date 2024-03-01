#!/usrl/bin/python3
"""
Script that takes in a URL and email, sends a POST request and decode in utf-8
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        urldt = sys.argv[1]
        email = sys.argv[2]
        encdt = bytes(parse.urlencode([("email", email)]), "utf-8")
        with request.urlopen(urldt, data=encdt) as urlres:
            print(urlres.read().decode("utf-8"))
