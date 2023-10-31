#!/usr/bin/python3
# shows the ASCII alphabet in reverse alternating in lower and uppercase

x = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - x)), end="")
    x = 32 if x == 0 else 0
