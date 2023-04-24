from read_data import getData


def parentsIn2Families(people):
    
    couples = set()
    parents = set()
    rec = 0

    for cpr, person in people.items():
        
        if person.getParents()!=[]:
            
            p1, p2 = person.getParents()[0], person.getParents()[1]

            couples.add((p1, p2))
            parents.add(p1)
            parents.add(p2)

    num_parents = len(list(parents))
    encountered = set() # Records parents encountered twice. We do not want people who have children with 3 or more people to be included in rec more than once

    for couple in couples:
        
        p1, p2 = couple[0], couple[1]
        
        if p1 not in parents and p1 not in encountered:
            rec += 1
            encountered.add(p1) # Record that the parent has been encountered, and should not further contribute to the percentage
        if p2 not in parents and p2 not in encountered:
            rec += 1
            encountered.add(p2)

        parents.discard(p1)
        parents.discard(p2)

    x = round(rec*100/num_parents)

    print(f"Percentage of people having children with 2 or more people: {x}%")

def main():

    people = getData()
    parentsIn2Families(people)

if __name__=="__main__":
    main()