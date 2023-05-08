from read_data import getData
from functions import *

def getInput():
    print("--------------------------------------------------")
    print("""1. Age and gender distribution of dataset.
2. Age distribution of first-time fatherhood.
3. Assessing normality of age distribution of first-time fatherhood.
4. Age distribution of first-time motherhood.
5. Assessing normality of age distribution of first-time motherhood.
6. Number of men and women without children.
7. Average age difference between parents.
8. Number of people with a living grandparent.
9. Average number of cousins.
10. Proportion of firsborn being female or male.
11. Number of people that have children with more than one partner.
12. Analysis of height differences between couples.
13. Do tall parents have tall children?
14. Analysis on BMI differences between couples.
15. Number of children being raised by non-biological parent (via bloodtype analysis).
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
    
    print("""Course: 22113 - Unix & Python Programming for Bioinformaticians

Project 5 - Data Analysis

Authors: Rolf Larsen and David Miles-Skov
""")

    people = getData()
    num = getInput()


    while num != 18:
        
        if num==1:
        
            age_gender_dist(people)

        if num==2:

            first_time_father_age(people)

        if num==3:

            ave_first_time_father_age(people)

        if num==4:
            
            first_time_mother_age(people)
        
        if num==5:
            
            ave_first_time_mother_age(people)

        if num==6:

            parenthood_percentage(people)

        if num==7:

            ave_parent_age_diff(people)

        if num==8:

            find_grandparents(people)

        if num==9:

            find_num_ave_cousins(people)
        
        if num==10:

            first_born_gender(people)

        if num==11:

            parents_w_2_familiesV2(people)
            

        if num==12:

            height_comparison_of_parents(people)

        if num==13:

            children_heights(people)

        if num==14:

            BMI_of_parents(people)
        
        if num==15:

            not_biological_parent(people)
        
        if num==16:

            fathers_that_can_donate_blood_to_sons(people)
        
        if num==17:

            can_donate_to_grandparents(people)

        if num==18:
            
            exit()

        num = getInput()

if __name__=="__main__":
    main()