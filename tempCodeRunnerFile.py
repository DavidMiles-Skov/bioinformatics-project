from read_data import getData
from functions import *

def getInput():
    print("--------------------------------------------------")
    print("""1. Age and gender distrubution.
2. Age distribution of first-time fatherhood.
3. Assessing normality of age distribution of first-time fatherhood.
4. Age distribution of first-time motherhood.
5. Assessing normality of age distribution of first-time motherhood.
6. Number of men and women without children.
7. Average age difference between parents.
8. Number of people with a living grandparent.
9. Average number of cousins.
10. Proportion of firsborn being female of male.
11. Number of people that have children with more than one partner.
12. Analysis of height differences between couples.
13. Do tall parents have tall children?
14. Analysis on BMI differences between couples.
15. Number of children being raises by non-biological parent (via bloodtype analysis).
16. Fathers that can donate blood to their sons.
17. People that can donate blood to at least one of their grandparents.
18. Exit Program.""")
    print("--------------------------------------------------")
    x=input("Enter number corresponding to desired exercise: ")
    while x not in [str(i) for i in range(1, 19)]: 
        x = input("Invalid input. Please try again: ")
    return int(x)


def main():
    
    # Setting up main data structure 
    
    people = getData()
    num = getInput()


    while num != 18:
        
        if num==1:
        
            ageAndGenderDist(people)

        if num==2:

            firstTimeFatherAge(people)

        if num==3:

            calcAveFirstTimeFatherAge(people)
        
        if num==18:
        
            exit()

        num = getInput()

if __name__=="__main__":
    main()