from read_data import getData

def canDonateTo(bt1, bt2):
    x_can_donate_to = {"A+": ["A+", "AB+"], "A-": ["A+", "A-", "AB+", "AB-"], "B+":["B+", "AB+"], "B-":["B+","B-","AB+","AB-"], "O+": ["A+","B+","O+","AB+"], "O-": ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], "AB+":["AB+"], "AB-":["AB+", "AB-"]}
    return bt2 in x_can_donate_to[bt1]

def personCanDonateBloodToGrandparents(people):

    person_to_grandparents = {}

    for cpr, person in people.items():
        
        if person.getParents()!=[]:

            p1, p2 = people[person.getParents()[0]], people[person.getParents()[1]]
            l = []        
            l.extend(p1.getParents())            
            l.extend(p2.getParents())            
            person_to_grandparents[cpr] = l

    personToGrandparentsBlood = {}

    for person, grandparents in person_to_grandparents.items():
        
    
        x = [i for i in grandparents if canDonateTo(people[person].getBloodType(), people[i].getBloodType())]
        
        if x !=[]:
        
            personToGrandparentsBlood[person] = x

    print(personToGrandparentsBlood)

def main():

    people = getData()
    personCanDonateBloodToGrandparents(people)

if __name__ =="__main__":
    main()


    

            