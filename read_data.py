from person import Person
import os
import copy

""" Testing data reading/formatting method:

- Will create Dictionary with CPR->Person object, to make accessing relatives easier

"""

def addParents(dict): 
    cpr_lst = dict.keys()
    new_dict = {}
    for i in cpr_lst: # O(n)
        c = copy.deepcopy(dict[i])
        for j in cpr_lst: # O(n)
            p = copy.deepcopy(dict[j])
            if i in p.Children: # O(1)
                c.addParent(j) 
        new_dict[i]=c
    return new_dict
            

def getData(filename=r"data\people.db"):

    """
    getData: Takes filename (str) as input and returns a dictionary of cpr->person object
    - Creates main datastructure this project will utilise
    """
    
    dict={}
    

    if os.path.exists(filename):
        # Reading lines and adding data to dictionary
        f = open(filename, "r")

        lines=f.readlines()[4:] # O(n)

        i = 0
        read=True

        while read: # O(n)
            person = Person()
            while i < len(lines): # O(n)
                if lines[i].strip()=="": # O(l)
                    dict[person.CPR] = person
                    i+=1
                    break # New person
                elif lines[i].startswith("CPR: "): # O(l)
                    cpr = lines[i][5:].strip()
                    person.setCPR(cpr)
                    if int(cpr[-1])%2==0: person.setGender("Female") 
                    else: person.setGender("Male")
                elif lines[i].startswith("First name: "): # O(l)
                    fname = lines[i][11:].strip()
                    person.setFirstName(fname)
                elif lines[i].startswith("Last name: "): # O(l)
                    lname = lines[i][10:].strip()
                    person.setLastName(lname)
                elif lines[i].startswith("Height: "): # O(l)
                    height=int(lines[i][8:].strip())
                    person.setHeight(height)
                elif lines[i].startswith("Weight: "): # O(l)
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
        return addParents(dict) # O(x^2) - x is number of keys in dict
    else:

        raise FileNotFoundError("Could not find: ", filename)
    
# Overall: O(l*n^2+x^2) ~ O(l*n^2) where l is the maximum line length, n is the number of lines in the file and x is the number of
# keys in the dictionary