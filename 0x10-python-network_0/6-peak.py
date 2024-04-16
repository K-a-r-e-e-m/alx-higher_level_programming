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
            peak = list_of_integers[i]

        if list_of_integers[i] >= list_of_integers[i + 1]:
            peak = list_of_integers[i]

    if list_of_integers[0] > peak:
        return list_of_integers[0]
    elif list_of_integers[len(list_of_integers) - 1] > peak:
        return list_of_integers[len(list_of_integers) - 1]
    else:
        return peak
