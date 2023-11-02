#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_arg = (len(sys.argv) - 1)
    print("{} arguments".format(num_arg))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format((i), sys.argv[i]))
