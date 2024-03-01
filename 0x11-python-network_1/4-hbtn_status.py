#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    urlres = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(urlres.text)}")
    print(f"\t- content: {urlres.text}")
