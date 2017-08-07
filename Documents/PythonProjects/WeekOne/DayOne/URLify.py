#!/usr/bin/python
#Remove Spaces and replace with %20

def URLify(str_one):
    url = list()
    
    #Set STR_ONE to list
    url = [letter for letter in str_one]

    #look for "spaces" in the list
    for x in xrange(len(str_one)):
        if url[x] == ' ':
            url[x] = "%20"
    return ''.join(url)

usrStr = raw_input()
newStr = URLify(usrStr)
print(newStr)
