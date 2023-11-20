#!/usr/bin/python3
output = ""
for x in range(ord('a'), ord('z') + 1):
    if chr(x) not in ['q', 'e']:
        output += chr(x)

print("{}".format(output), end="")
