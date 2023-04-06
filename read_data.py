from person import Person
import os
import copy

""" Testing data reading/formatting method:

- Will create Dictionary with CPR->Person object, to make accessing relatives easier

"""
# TO BE IMPLEMENTED
# def addParents(dict):
#     # Iterate through dictionary
#     for cpr, person in dict.items():
#         if person.Children != []: # If a person has Children
#             print("Found person with children:\n")
#             print(person)
#             for child in person.Children: # Iterate through children
#                 dict[child].addParent(cpr) # Add parent cpr to child
#                 # print(f"Parent successfully added to child {child}. Checking:\n")
#                 # print(dict[child])
#                 # print()
#                 break # Only need to iterate over first child, calling add parent to first child will do so for all children?! Very strange
#             # To check with Peter, I have no idea why this is the case         
#             # print("Checking very weird behaviour:\n")
#             # for child in person.Children:
#             #     print(child)
#             #     print(dict[child])
#             # exit()
#     return dict


# Trying different method - Will be much more inefficient, but should hopefully be correct
def addParents(dict): 
    cpr_lst = dict.keys()
    new_dict = {}
    for i in cpr_lst: # O(n)
        c = copy.deepcopy(dict[i])
        for j in cpr_lst: # O(n)
            p = copy.deepcopy(dict[j])
            if i in p.Children:
                c.addParent(j)
        new_dict[i]=c
    return new_dict
            

def getData(filename=r"data\people.db"):
    
    dict={}
    

    if os.path.exists(filename):
        # Reading lines and adding data to dictionary
        f = open(filename, "r")

        lines=f.readlines()[4:]

        i = 0
        read=True

        while read:
            person = Person()
            while i < len(lines):
                if lines[i].strip()=="":
                    dict[person.CPR] = person
                    i+=1
                    break # New person
                elif lines[i].startswith("CPR: "):
                    cpr = lines[i][5:].strip()
                    person.setCPR(cpr)
                    if int(cpr[-1])%2==0: person.setGender("Female")
                    else: person.setGender("Male")
                elif lines[i].startswith("First name: "):
                    fname = lines[i][11:].strip()
                    person.setFirstName(fname)
                elif lines[i].startswith("Last name: "):
                    lname = lines[i][10:].strip()
                    person.setLastName(lname)
                elif lines[i].startswith("Height: "):
                    height=int(lines[i][8:].strip())
                    person.setHeight(height)
                elif lines[i].startswith("Weight: "):
                    weight=int(lines[i][8:].strip())
                    person.setWeight(weight)
                elif lines[i].startswith("Eye color: "):
                    eyecolor=lines[i][10:].strip()
                    person.setEyeColor(eyecolor)
                elif lines[i].startswith("Blood type: "):
                    bloodtype=lines[i][11:].strip()
                    person.setBloodType(bloodtype)
                elif lines[i].startswith("Children: "):
                    children=lines[i][9:].split()
                    person.addChildren(children)
                else:
                    pass
                i+=1
            if i >= len(lines): read = False
        return dict
    else:

        raise FileNotFoundError("Could not find: ", filename)