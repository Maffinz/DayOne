#!/usr/bin/python

def isStringDiff(str_one,str_two):
    if len(str_one) > len(str_two):
        size = len(str_two)
    else:
        size = len(str_one)

    for i in xrange(size):
        if str_one[i] != str_two[i]:
            return True
    return False


