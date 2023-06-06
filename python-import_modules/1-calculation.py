#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    addition = add(a, b)
    print("{} + {} = {}".format(a, b, addition), end="\n")

    substraction = sub(a, b)
    print("{} - {} = {}".format(a, b, substraction), end="\n")

    multiplication = mul(a, b)
    print("{} * {} = {}".format(a, b, multiplication), end="\n")

    division = div(a, b)
    print("{} / {} = {}".format(a, b, division), end="\n")
