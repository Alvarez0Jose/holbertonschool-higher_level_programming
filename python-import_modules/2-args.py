#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = sys.argv[1:]
    args_count = len(args)

    if args_count == 0:
        print("{} arguments.".format(args_count))
    elif args_count == 1:
        print("{} argument:".format(args_count), end="\n")
        print(f"{args_count}:", "".join(args), end="\n")
    else:
        print(f"{args_count} arguments:", end="\n")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}", end="\n")
