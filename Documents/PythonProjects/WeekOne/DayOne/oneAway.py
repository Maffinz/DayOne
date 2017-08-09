#!/usr/bin/python

#Given Two string, weite a function to check if they are one edir or zero edits away..
#Return True if:  No Changes, One Change(Insertion,Deletion,replace)
#REturn False if: Two or more changes are made..

def oneAway(str_one,str_two):
    if len(str_one) != len(str_two):
        largestStr = None
        smallestStr = None
        if len(str_one) > len(str_two):
            largestStr = str_one
            smallestStr = str_two
        else:
            largestStr = str_two
            smallestStr = str_one

        for curChar in smallestStr:
            inString = False
            for seek in largestStr:
                if curChar == seek:
                    inString = True
                    break
            if inString == False:
                return False
        return True
    else:
        if str_one == str_two:
            return True
        mods = 0
        for index in xrange(len(str_one)):
            if str_one[index] != str_two[index]:
                mods += 1
            if mods > 1:
                return False
        return True

str1 = raw_input("String 1: ")
str2 = raw_input("String 2: ")
print(oneAway(str1,str2))
