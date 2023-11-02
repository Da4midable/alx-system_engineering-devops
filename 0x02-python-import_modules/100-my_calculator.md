#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    num_arg = (len(sys.argv) - 1)
    if num_arg > 1 and num_arg != 3:
        print("{} arguments:".format(num_arg)) 
    elif num_arg == 1:
        print("{} argument:".format(num_arg))
    elif num_arg == 0:
        print("{} arguments.".format(num_arg))
    elif num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    for i in range(1, len(sys.argv)):
        a = int(sys.argv[i])
        b = int(sys.argv[i+1])
        print("{}: {}".format((i), sys.argv[i])) 
        res_add = add(a, b)
        res_sub = sub(a, b)
        res_mul = mul(a, b)
        res_div = div(a, b)
        if res_add:
            print("{:d} + {:d} = {:d}".format(a, b, res_add))
        if res_sub:
            print("{:d} - {:d} = {:d}".format(a, b, res_sub))
        if res_mul:
            print("{:d} * {:d} = {:d}".format(a, b, res_mul))
        if res_div:
            print("{:d} / {:d} = {:d}".format(a, b, res_div))
