#!/usr/bin/python3
"""
Script that takes my GitHub details and uses the GitHub API to display my id
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        urldt = "https://api.github.com/user"
        username = sys.argv[1]
        password = sys.argv[2]
        api_headers = {
                "Accept": "application/vnd.github.v3+json",
                "Username": username,
                "Authorization": f"token {password}"
        }
        urlres = requests.get(urldt, headers=api_headers)
        urlstatus = urlres.status_code
        if urlstatus == 200:
            github_user = urlres.json()
            if github_user["login"] == username:
                print(github_user["id"])
            else:
                print("None")
        else:
            print("None")
