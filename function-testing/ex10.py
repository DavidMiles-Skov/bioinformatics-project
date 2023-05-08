from read_data import getData

def firstBornGender(people):
    """
    - Will calculate female/male percentages of firstborn children
    Method:
    - initialise empty sums for the two genders and set of parents
    - Iterate through people:
        - If person has children and not in encountered parent set:
            - Sort list of children based on 4,5 index of cpr string (lambda function)
            - Check gender of first born (lowest birth year)
            - Add 1 to correct sum
            - Find partner of current person (other parent), add the two parents' cprs to set of parents
    """
    
    f_firstborn=0
    m_firstborn=0
    encountered_parents = set()


    for cpr, person in people.items():
        
        if person.getChildren()!=[] and cpr not in encountered_parents:
            
            children_cprs = person.getChildren()
            children_cprs.sort(key=lambda x: (x[4:6], x[2:4], x[:2])) # Using lambda function to sort by birth year
            firstborncpr=children_cprs[0]
            
            if people[firstborncpr].getGender()=="Male":
                m_firstborn+=1
            else:
                f_firstborn+=1
            
            encountered_parents.add(cpr)
            
            # Find other parent
            
            otherparent=[i for i in people[firstborncpr].getParents() if i != cpr][0]
            encountered_parents.add(otherparent)
    
    return f"Gender:\tPercentage firstborn:\nMale:\t{round(100*m_firstborn/(m_firstborn+f_firstborn),2)}%\nFemale:\t{round(100*f_firstborn/(m_firstborn+f_firstborn),2)}%"

def main():
    
    people = getData()
    print(firstBornGender(people))

if __name__=="__main__":

    main()



