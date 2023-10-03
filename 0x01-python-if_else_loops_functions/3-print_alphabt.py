#!/usr/bin/python3
for k in range(ord('a'), ord('z') + 1):
    if chr(k) != 'q' and chr(k) != 'e':
        print('{:c}'.format(k), end='')
