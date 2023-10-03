#!/usr/bin/python3
flag = 0
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        ch = i
    else:
        ch = i - 32

    print('{:c}'.format(ch), end='')
