#!/usr/bin/python

def isPermutate(str_one,str_two):
    #Takes X to solve the problem
    #str_one and str_two are same size

    for i in xrange(len(str_one)):
        seek = str_one[i]
        found = False
        for x in xrange(len(str_two)):
            if seek == str_two[x]:
                found = True
                break
        if found == False:
            return False
    return True
