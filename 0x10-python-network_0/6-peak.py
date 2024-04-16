#!/usr/bin/python3
# Make a find_peak function that find a peak.
'''
This module have a functoin find_peak that find the peak
of numbers in unsorted list
'''


def find_peak(list_of_integers):
    '''Finds the peak in a list of unsorted numbers.'''

    if list_of_integers == []:
        return

    check1 = True
    check2 = True
    peak = list_of_integers[0]

    for i in range(1, len(list_of_integers) - 1):

        if list_of_integers[i - 1] <= list_of_integers[i]:
            check1 = True
            peak = list_of_integers[i]
        else:
            check1 = False

        if list_of_integers[i] >= list_of_integers[i + 1]:
            check2 = True
            peak = list_of_integers[i]
        else:
            check2 = False

    if check1 and check2:
        return peak
