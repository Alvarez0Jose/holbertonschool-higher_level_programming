#!/usr/bin/python3
output = ''
for i in range(ord('a'), ord('z')+1):
    output += "{}"

print(output.format(*[char(i) for i in range(ord('a'), ord('z')+1)]))
