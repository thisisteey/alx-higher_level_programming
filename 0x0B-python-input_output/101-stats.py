#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
from sys import stdin

filesz = 0
x = 0
stat_cds = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in stdin:
        tkns = line.split()
        if len(tkns) >= 2:
            y = x
            if tkns[-2] in stat_cds:
                stat_cds[tkns[-2]] += 1
                x += 1
            try:
                filesz += int(tkns[-1])
                if y == x:
                    x += 1
            except FileNotFoundError:
                if y == x:
                    continue
        if x % 10 == 0:
            print(f"File size: {filesz:d}")
            for key, val in sorted(stat_cds.items()):
                if val:
                    print(f"{key:s}: {val:d}")
    print(f"File size: {filesz:d}")
    for key, val in sorted(stat_cds.items()):
        if val:
            print(f"{key:s}: {val:d}")

except KeyboardInterrrupt:
    print(f"File size: {filesz:d}")
    for key, val in sorted(stat_cds.items()):
        if val:
            print(f"File size: {filesz:d}")
