from person import Person
import os

""" Testing data reading/formatting method:

- Will create Dictionary with CPR->Person object, to make accessing relatives easier

"""

def getData(filename):
    
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