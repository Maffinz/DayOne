#!/usr/bin/python

def isPermutate(str_one,str_two):
    startOn = 0
    for fChar in str_one:
        for ite in xrange(len(str_two)):
            if fChar == str_two[ite + startOn]:
                if (ite+startOn) == len(str_two):
                    str_two = str_two[:ite+startOn]
                elif (ite+startOn) == 0:
                    str_two = str_two[1:]
                else:
                    str_two = str_two[:ite+startOn] + str_two[ite+startOn+1:]
            else:
                return False
    return True


str_one = raw_input("String1: ")
str_two = raw_input("String2: ")
print(isPermutate(str_one,str_two))
