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
    list_of_integers.sort()
    return list_of_integers[-1]
