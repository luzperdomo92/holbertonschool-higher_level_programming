#!/usr/bin/python3
if __name__ == "__main__":
    import sys 

args = len(sys.argv)

if args == 1:
    print("0 arguments.")
elif args == 2:
    print("{} argument:".format(args - 1))
    print("{}: {}".format(1, sys.argv[1]))
else:
    print("{} arguments:".format(args - 1))
    for argm in range(1, args)
        print("{} : {}".format(argm, sys.args[argm]))
