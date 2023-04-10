from read_data import getData



def findGrandParents(people):

    num_people_w_grandparents = 0

    for cpr, person in people.items():
        
        if person.Parents != []: 
            for parent_cpr in person.Parents:
                parent = people[parent_cpr]
                if parent.Parents!=[]:
                    num_people_w_grandparents+=1
    print(len(people.keys()))
    print(f"{num_people_w_grandparents} people have a living grandparent, corresponding to {round(num_people_w_grandparents/len(people.keys()),2)*100}% of the data")

def main():
    
    people=getData()
    findGrandParents(people)

if __name__=="__main__":
    main()