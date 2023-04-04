import re

class Person():

    def __init__(self, cpr="", firstname="", lastname="", height=None, weight=None, eyecolor="", bloodtype="", children=[],gender=None,parents=[]):
        self.CPR = cpr
        self.FirstName=firstname
        self.LastName=lastname
        self.Height=height
        self.Weight=weight
        self.EyeColor=eyecolor
        self.BloodType=bloodtype
        self.Children=children
        self.Gender=gender
        self.Parents=parents


    # Setters for attributes

    def setCPR(self, cpr):
        cpr_regex=r"\d{6}-\d{4}"
        if re.match(cpr_regex, cpr):
            self.CPR=cpr
        else:
            raise ValueError("Invalid CPR number given: ", cpr)


    def setFirstName(self, name):
        if isinstance(name, str):
            self.FirstName=name
        else:
            raise TypeError("Name must be of type string")
        
    def setLastName(self, name):
        if isinstance(name, str):
            self.LastName=name
        else:
            raise TypeError("Name must be of type string")
    
    def setHeight(self, height):
        if isinstance(height, int): 
            self.Height=height
        else:
            raise TypeError("Height must be of type int")
    
    def setWeight(self, weight):
        if isinstance(weight, int): 
            self.Weight=weight
        else:
            raise TypeError("Weight must be of type int")
        
    def setEyeColor(self, eyecolor):
        if isinstance(eyecolor, str):
            self.EyeColor=eyecolor
        else:
            raise TypeError("Eye color must be of type string")
        
    def setBloodType(self, bloodtype):
        if bloodtype in ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]:
            self.BloodType=bloodtype
        else:
            raise ValueError("Invalid blood type.")
    
    def setGender(self, gender):
        if gender not in ["Male", "Female"]: raise ValueError("Invalid gender given")
        self.Gender=gender

    def addChildren(self, children):
        if isinstance(children, list) and all(isinstance(item, str) for item in children):
            self.Children = children
        else:
            raise TypeError("Method requires list of strings (cpr-numbers) as argument")

    def addParent(self, parent):
        if len(self.Parents)==2:
            raise Exception("Cannot have more than two parents")
        cpr_regex=r"\d{6}-\d{4}"
        if not re.match(cpr_regex, parent):
            raise ValueError("Parent must be a string of a CPR number")
        self.Parents.append(parent)
            
        
    
    def __str__(self):
        s = f"CPR: {self.CPR}\nName: {self.FirstName} {self.LastName}\nGender: {self.Gender}\nHeight: {self.Height}\nWeight: {self.Weight}\nEye color: {self.EyeColor}\nBlood type: {self.BloodType}\nChildren: {self.Children}\nParents: {self.Parents}"
        return s
    
