#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to a url
"""
import requests
import sys


if __name__ == "__main__":
    urldt = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        urlqry = sys.argv[1]
    else:
        urlqry = ""
    encdt = [("q", urlqry)]
    urlres = requests.post(urldt, data=encdt)
    try:
        jsondt = urlres.json()
        if jsondt:
            print(f"[{jsondt['id']}] {jsondt['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
