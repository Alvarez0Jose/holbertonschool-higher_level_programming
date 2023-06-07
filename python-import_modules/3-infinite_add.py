#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    idx = []
    for i in args:
        idx.append(int(i))

    result = sum(idx)
    print(result, end="\n")
