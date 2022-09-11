#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    numarg = len(sys.argv) - 1

    if numarg == 0:
        print("0 arguments.")

    elif numarg == 1:
        print("1 argument:".format(numarg))

    else:
        print("{} arguments:".format(numarg))

        for index in range(numarg):
            print("{:d}: {}".format(index + 1, sys.argv[index + 1]))
