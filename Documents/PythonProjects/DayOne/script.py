#!/usr/bin/python
import json
import sys
"""Write and Read from file"""

class Employee:
    def __init__(self, name,salary,workID):
        self.name = name
        self.salary = salary
        self.workID = workID

class Developer(Employee):
    def __init__(self, name,salary,workdID,prog_lang):
        Employee.__init(name,salary,workID)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, name,salary,workID,devs):
        Employee.__init__(name,salary,workID)
        self.devs = devs

def writeError(typeError,data):
    outFile = open("ErrorData.dat","a+")
    outFile.write("Failed to continue at '{}' , user input: {}\n".format(typeError, data))
    outFile.close()

def writeManager(emp):
    outFile = open("manager.dat","a+")
    outFile.write(str(emp))
    outFile.close()
def writeDeveloper(emp):
    outFile = open("developer,dat","a+")
    outFile.write(str(emp))
    outFile.close()
def lookUpEmployee(workID):
    with open("employees.dat","r") as fileInput:
        for line in fileInput:
            out = line.split()
            employees

def getManager():
    manager = eval(open("manager.dat","r").read()


manager = dict()
group = list()
lang = list()
devs = dict()

print("1. Log In")
print("2. Register")
print("3. Look Up")
print("4. Exit")

usrChoice = int(raw_input("Choice: "))
if usrChoice == 1:
    typeUser = raw_input("(M)anager / (D)eveloper: ")
    if typeUser != "M" or typeUser != "D":
        writeError("Type User", typeUSer)
        sys.exit(0)
    ID = int(raw_input("WorkID: "))
    #Look For ID in the Manager or Developer Dictionary and set the name, salary, workID, devs/lang

elif usrChoice == 2:
    regType = raw_input("(M)anager or (D)eveloper): ")
    name = raw_input("Name: ")
    salary = input("Salary: ")
    workID: input("Work-ID: ")
    if regType = "M":
        for name in xrange(5):
            group.append(name)
        obj = Manager(name,salary,workID,group)
        manager.update('name',list.append(obj.name))
        manager.update('salary',list.append(obj.salary))
        manager.update('workID',list.append(obj.workID))
        manager.update('devs',list.append(list.append(group)))
        writeManager(manager)

    elif regType = "D":
        for prog_lang in xrange(5):
            lang.append(prog_lang)
        obj = Developer(name,salary,workdID,lang)
        devs.update('name',list.append(obj.name))
        devs.update('salary',list.append(obj.salary))
        devs.update('workID',list.append(obj.workdID))
        devs.update('langs',list.append(list.append(lang)))
        writeDeveloper(devs)
elif usrChoice == 3:
    
elif usrChoice == 4:
    
else:
    writeError("Menu", usrChoice)
    sys.exit(0)

