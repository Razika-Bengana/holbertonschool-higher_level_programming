#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    total = 0

    for args in argv[1:]:
            total += int(args)
            print("{:d}".format(total))
