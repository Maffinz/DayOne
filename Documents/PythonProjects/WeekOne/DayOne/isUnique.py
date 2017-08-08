#!/usr/bin/python

def isUnique(str_one):
    startOn = 1
    for char in str_one:
        for ite in xrange(len(str_one)- startOn):
            if str_one[startOn + ite] == char:
                return False
        startOn += 1
    return True
    #Slow way?


usrInput = raw_input("String: ")
print(isUnique(usrInput))

#Slow solution...?
