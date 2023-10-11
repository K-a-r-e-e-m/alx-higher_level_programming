#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    from sys import argv

    sum = 0
    for i in range(1, len(argv)):
        sum = add(int(argv[i]), sum)
    print(sum)
