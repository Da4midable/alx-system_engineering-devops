#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res_add = 0
    for i in range(1, len(sys.argv)):
        res_add += int(sys.argv[i])
    print("{:d}".format(res_add))
