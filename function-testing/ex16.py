from read_data import getData

def canDonateTo(bt1, bt2):
    x_can_donate_to = {"A+": ["A+", "AB+"], "A-": ["A+", "A-", "AB+", "AB-"], "B+":["B+", "AB+"], "B-":["B+","B-","AB+","AB-"], "O+": ["A+","B+","O+","AB+"], "O-": ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], "AB+":["AB+"], "AB-":["AB+", "AB-"]}
    return bt2 in x_can_donate_to[bt1]

def fathersBloodDonateToSons(people):
    """Will create a dictionary of father -> list of sons that can receive blood from father
    Method:
        Iterate through people dict, make list of father cprs
        intialise empty dict 
        Iterate through father cprs
            create key of cpr in dict with value of empty list
            Iterate through children, Check if father can donate blood
                if yes then append child cpr to value of dict
    
                else pass
    """
    
    father_cprs = [i for i,x in people.items() if x.getGender()=="Male" and len(x.getChildren())>0]
    fToSDonate = {}

    for father_cpr in father_cprs:
        
        fToSDonate[father_cpr] = []
        father = people[father_cpr]
        
        for child_cpr in father.getChildren():
            
            child = people[child_cpr]
            
            if canDonateTo(father.getBloodType(), child.getBloodType()) and child.getGender()=="Male":
                fToSDonate[father_cpr].append(child_cpr)
    
    for father, sons in fToSDonate.items():
        print(f"Father {father} can donate to: {sons}")

def main():

    people=getData()
    fathersBloodDonateToSons(people)

if __name__=="__main__":
    main()

