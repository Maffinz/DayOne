#!/usr/bin/python

def isPermutate(str_one,str_two):
    for fChar in str_one:
        tempSize = len(str_two)
        for ite in xrange(tempSize):
            if fChar == str_two[ite]:
                if ite == len(str_two):
                    str_two = str_two[:ite]
                    break
                elif ite == 0:
                    str_two = str_two[1:]
                    break
                else:
                    str_two = str_two[:ite] + str_two[ite+1:]
                    break
        if tempSize == len(str_two):
            return False
    return True


str_one = raw_input("String1: ")
str_two = raw_input("String2: ")
print(isPermutate(str_one,str_two))
