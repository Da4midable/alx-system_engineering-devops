#!/usr/bin/python3
for x in range((0), (9) + 1):
    for y in range(x + 1, 10):
        if x != 8 or y != 9:
            print("{}".format(x) + "" + "{}".format(y), end=", ")
print("{:02d}".format(89))
