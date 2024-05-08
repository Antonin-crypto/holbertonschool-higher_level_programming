#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    sum = 0
    argument = argv[1:]
    for args in argument:
        sum += int(args)

    print("{}".format(sum))
