#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import*
    from sys import argv

    if len(argv) - 1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit (1)
    elif argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit (1)
    else:
        print('{} {} {} = '.format(argv[1], argv[2], argv[3]), end='')
        if argv[2] == '+':
            print(int(argv[1]) + int(argv[3]))
        elif argv[2] == '-':
            print(int(argv[1]) - int(argv[3]))
        elif argv[2] == '*':
            print(int(argv[1]) * int(argv[3]))
        elif argv[2] == '/':
            print(int(argv[1]) / int(argv[3]))
