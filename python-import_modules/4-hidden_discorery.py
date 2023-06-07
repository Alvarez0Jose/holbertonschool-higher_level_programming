#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    word = dir(hidden_4)
    word_filter = []

    for chr in word:
        if not chr.startswith('__'):
            word_filter.append(chr)

    word_filter.sort()

    for chr in word_filter:
        print(chr)
