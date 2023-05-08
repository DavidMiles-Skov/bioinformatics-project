from read_data import *
import matplotlib.pyplot as plt
from collections import Counter




######################## Functions for exercise 1 ########################

def add_age(age, target_dict, amount=1):
    if age>=16 and age<=20:
        target_dict["16-20"]+=amount
    elif age>=21 and age<=25:
        target_dict["21-25"]+=amount
    elif age>=26 and age<=30:
        target_dict["26-30"]+=amount
    elif age>=31 and age<=35:
        target_dict["31-35"]+=amount
    elif age>=36 and age<=40:
        target_dict["36-40"]+=amount
    elif age>=41 and age<=45:
        target_dict["41-45"]+=amount
    else:
        target_dict["46+"]+=amount
    return target_dict
        
def calc_age_dist_DK(filepath=r"data\DKpopulation.csv"):
    data = open(filepath, "r")
    male_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }
    female_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }
    data = data.readlines()[1:]
    for line in data:
        l = line.split(";")
        age = int(l[1].split()[0])
        gender = l[2]
        amount=int(l[-1])
        
        if gender=="Men": add_age(age, male_ages, amount=amount)
        elif gender=="Women": add_age(age, female_ages, amount=amount)
        else: raise Exception("Error in determining gender")

    total_male = sum(male_ages.values())
    total_female = sum(female_ages.values())

    # Converting from numbers to percentages

    male_prop = {agerange: round((num/total_male)*100,2) for agerange, num in male_ages.items()}
    female_prop = {agerange: round((num/total_female)*100, 2) for agerange, num in female_ages.items()}
    
    return male_prop, female_prop
    
def calc_age_dist_DATA(people):
    """
    Calculates the age distribution of the test data
    
    """
    male_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }
    female_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }

    for cpr, person in zip(people.keys(), people.values()): # O(x)
        age = 100-int(cpr[4:6])

        if person.getGender()=="Male": male_ages = add_age(age, male_ages) # O(1)
        else: female_ages = add_age(age, female_ages)
    
    total_male = sum(male_ages.values()) # O(x)
    total_female = sum(female_ages.values()) # O(x)

    # Converting from numbers to percentages

    male_prop = {agerange: round((num/total_male)*100,2) for agerange, num in male_ages.items()}
    female_prop = {agerange: round((num/total_female)*100, 2) for agerange, num in female_ages.items()}
    
    return male_prop, female_prop

# Overall: O(x)

# Final function 

def age_gender_dist(people):
    
    m_ages_test, f_ages_test = calc_age_dist_DATA(people)
    m_ages_data, f_ages_data = calc_age_dist_DK()

    print("------Comparing age and gender distributions------")
    print("Age range:\nGender:\tpeople.db \t DKpopulation.csv")
    
    for ages in m_ages_test.keys(): # O(x)
        #print(f"{ages}:\nM: {m_ages_test[ages]}%\t{m_ages_data[ages]}%\nF: {f_ages_test[ages]}%\t{f_ages_data[ages]}%")
        print(f"{ages}:\nM: {m_ages_test[ages]}%\t{m_ages_data[ages]}%\nF: {f_ages_test[ages]}%\t{f_ages_data[ages]}%")
    print("Conclusion: Age and gender distribution very similar to that of the Danish population (2023).")

########################################################################


######################## Functions for exercise 2 ########################

def first_time_father_age(people):
    """
    Will calculate the age at which fathers have their first child.
    - Father: XXXXFF-XXXX
    - Eldest Child: XXXXCC-XXXX
    - Age at fatherhood: CC-FF
    """
    ages = []

    for person in people.values(): # O(x)
        if person.getChildren() != [] and person.getGender()=="Male":
            yFather = int(person.getCPR()[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.getChildren()]) # O(c)
            ages.append(eldest-yFather)
    ages.sort() # O(log(x))
    counter = Counter(ages)
    age_vals = [i for i in counter.keys()]
    print(f"Minimum Age: {min(ages)}\nMaximum Age: {max(ages)}\nMean Age: {round(sum(ages)/len(ages), 2)}")
    prop = [i/len(ages) for i in counter.values()]
    x = input("Display Histogram graphically? (requires matplotlib) Y/N: ")
    while x not in ["Y", "N"]:
        x = input("Display Histogram graphically? (requires matplotlib) Y/N: ")
    if x=="Y":
        plt.bar(age_vals, prop)
        plt.xlabel("Age of first-time fatherhood")
        plt.ylabel("Proportion")
        plt.xticks(age_vals)
        plt.title("Distribution of ages of first-time fatherhood")
        plt.show()
    else:
         print("Age:\tPercentage:")
         for age, proportion in zip(age_vals, prop):
              print(f"{age}:\t{round(proportion*100, 2)}%")
              

##########################################################################

######################## Functions for exercise 3 ########################

def ave_first_time_father_age(people):
    """
    Will calculate the average age at which fathers have their first child.
    - Father: XXXXFF-XXXX
    - Child: XXXXCC-XXXX
    - Age at fatherhood: CC-FF
    """
    ages = []

    for person in people.values():
        if person.getChildren() != [] and person.getGender()=="Male":
            yFather = int(person.getCPR()[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children]) # O(c)
            ages.append(eldest-yFather)
    x = 31.3 # Average age of first-time fathers in denmark according to statistics denmark
    print("--------------Comparison of mean age of first-time fatherhood----------------")
    print(f"Test data: {round(sum(ages)/len(ages), 1)}\nData from Statistics Denmark: {x}")
    print("Conclusion: Much lower than average. However, not inconceivable.")

##########################################################################

######################## Functions for exercise 4 ########################

def first_time_mother_age(people):
    """
    Will calculate the age at which Mothers have their first child.
    - Father: XXXXFF-XXXX
    - Child: XXXXCC-XXXX
    - Age at motherhood: CC-FF
    """
    ages = []

    for _, person in people.items():
        if person.getChildren() != [] and person.getGender()=="Female":
            yMother = int(person.getCPR()[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yMother)
    ages.sort()
    counter = Counter(ages)
    age_vals = [i for i in counter.keys()]
    prop = [i/len(ages) for i in counter.values()]
    print(f"Minimum Age: {min(ages)}\nMaximum Age: {max(ages)}\nMean Age: {round(sum(ages)/len(ages), 2)}")
    x = input("Display Histogram graphically? (requires matplotlib) Y/N: ")
    while x not in ["Y", "N"]:
        x = input("Display Histogram graphically? (requires matplotlib) Y/N: ")
    if x=="Y":
        plt.bar(age_vals, prop, color="r")
        plt.xlabel("Age of first-time motherhood")
        plt.ylabel("Proportion")
        plt.xticks(age_vals)
        plt.title("Distribution of ages of first-time motherhood")
        plt.show()
        return
    else:
         print("Age:\tPercentage:")
         for age, proportion in zip(age_vals, prop):
              print(f"{age}:\t{round(proportion*100, 2)}%")

##########################################################################

######################## Functions for exercise 5 ########################

def ave_first_time_mother_age(persondict):
    """
    Will calculate the age at which mothers have their first child.
    - Father: XXXXFF-XXXX
    - Child: XXXXCC-XXXX
    - Age at motherhood: CC-FF
    """
    ages = []

    for person in persondict.values():
        if person.Children != [] and person.Gender=="Female":
            yFather = int(person.CPR[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yFather)
    x = 28.9 # Average age of first-time mothers in denmark according to statistics denmark
    print("--------------Comparison of mean age of first-time motherhood----------------")
    print(f"Test data: {round(sum(ages)/len(ages), 1)}\nData from Statistics Denmark (2006): {x}")
    print("Conclusion: Much lower than average. However, not unreasonable.")

##########################################################################

######################## Functions for exercise 6 ########################

def parenthood_percentage(people):                          #Needs to be updated to the proper path, this was just made from own directory
	"""Percentage of males and females who are not parents"""
	males, females = [], []


	for person in people.values(): # O(x)                                                                #Iterating over the person class values in the getData dict
		#"1" means they have children, "0" means they do not have children
		if person.getGender() == "Male" and len(person.getChildren()) != 0: males.append("1")          
		elif person.getGender() == "Male" and len(person.getChildren()) == 0: males.append("0")
		if person.getGender() == "Female" and len(person.getChildren()) != 0: females.append("1")
		elif person.getGender() == "Female" and len(person.getChildren()) == 0: females.append("0")


	Number_of_males = len(males)
	Number_of_females = len(females)


	Non_fathers = males.count("0")
	Non_mothers = females.count("0") # O(x)

	print("Percentage of men not fathers: " + str(round((Non_fathers/Number_of_males)*100, 2)), "% percentage of women not mothers: " + str(round((Non_mothers/Number_of_females)*100, 2))+"%")


##########################################################################

######################## Functions for exercise 7 ########################

def ave_parent_age_diff(people):
    
    encountered_children = set()
    differences = []
    
    for cpr, person in people.items(): # O(x)
        

        parents = person.getParents()


        if parents != [] and cpr not in encountered_children: # O(c)
        
            p1 = people[parents[0]]
            p2 = people[parents[1]]
            diff = abs(int(p1.getCPR()[4:6])-int(p2.getCPR()[4:6]))
            differences.append(diff)

            # Making sure that mother/father pair are not added to list again

            for child in p1.getChildren():
                encountered_children.add(child)


    print(f"Average age differences between parents in data: {round(sum(differences)/len(differences), 2)}")

##########################################################################

######################## Functions for exercise 8 ########################

def find_grandparents(people):

    num_people_w_grandparents = 0

    for cpr, person in people.items(): # O(x) - Iterating through grandchildren
        if person.getParents() != []: 
            for parent_cpr in person.getParents(): # O(p) - Iterating through grandchilds' parents
                parent = people[parent_cpr]
                if parent.getParents()!=[]: # O(m) - If  child->parent->grandparent exits, add 1
                    num_people_w_grandparents+=1
                    
    # print(len(people.keys()))
    print(f"{num_people_w_grandparents} people have a living grandparent, corresponding to {round(num_people_w_grandparents/len(people.keys()),2)*100}% of the data")

##########################################################################

######################## Functions for exercise 9 ########################

def find_num_ave_cousins(dict):
    """
    - Takes dictionary of cpr->person and returns average number of cousins (float)
    - Cousins are found via:
        - Initialise empty set to keep track of traversed parents/uncles/aunts
        - For each person in the dictionary (grandparents)
            - if grandparents not considered:
                - add grandparents to set
                - Initialise sum = 0 (sum represents number of cousins in current family)
                - For every child of that person (parents/uncles/aunts)
                    - sum += number of children for current child 
                - append sum to list 
        - return average of list
    """

    num_cousins = []
    considered_grandparents = set()

    for cpr,grandparent in dict.items(): # O(x)
        if grandparent.getChildren() !=[] and cpr not in considered_grandparents: # Person has children and family that has not already been considered
            # Finding person's partner
            c1 = dict[grandparent.Children[0]] 
            partner = [i for i in c1.getParents() if i != cpr][0]
            # Adding grandparents to set
            considered_grandparents.add(cpr)
            considered_grandparents.add(partner)
            parent_cprs = grandparent.getChildren()
            cousins = 0
            for p_cpr in parent_cprs: # iterating through parents, O(p)
                cousins += len(dict[p_cpr].getChildren()) # Summing up number of cousins: Number of children each sibling has
            num_cousins.append(cousins)
    print(f"Average number of cousins: {round(sum(num_cousins)/len(num_cousins),2)}")

##########################################################################

######################### Functions for exercise 10 #########################

def first_born_gender(people):
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


    for cpr, person in people.items(): # O(x) x = people
        
        if person.getChildren()!=[] and cpr not in encountered_parents: # O(s) s = set
            
            children_cprs = person.getChildren()
            children_cprs.sort(key=lambda x: (x[4:6], x[2:4], x[:2])) # Using lambda function to sort by birth year. # O(c) c = children
            firstborncpr=children_cprs[0]
            
            if people[firstborncpr].getGender()=="Male":
                m_firstborn+=1
            else:
                f_firstborn+=1
            
            encountered_parents.add(cpr)
            
            # Find other parent - family is not accounted for >1 times
            
            otherparent=[i for i in people[firstborncpr].getParents() if i != cpr][0] # O(2) max.
            encountered_parents.add(otherparent)
    
    print(f"Gender:\tPercentage firstborn:\nMale:\t{round(100*m_firstborn/(m_firstborn+f_firstborn),2)}%\nFemale:\t{round(100*f_firstborn/(m_firstborn+f_firstborn),2)}%")
    print("According to these percentages, it is more likely that the firstborn will be female.")

##########################################################################

######################### Functions for exercise 11 #########################


# def parents_w_2_familiesV3(people):
#     parents = set()
#     couples = set()
#     for _, person in people.items():
#         for parent in person.getParents():
#              parents.add(parent)
#     my_dict = {i:list(parents).count(i) for i in list(parents)}
#     print(my_dict)

def parents_w_2_familiesV2(people):
     
     couples = set()

     for _, person in people.items():
          
          if person.getParents()!=[]:
               parents = person.getParents()
               # sort according to cpr
               parents.sort(key= lambda x: (x[4:6], x[2:4], x[:2]))
               p1, p2 = parents[0], parents[1]
               couples.add((p1,p2))
     
     list_of_parents = list()
     for couple in couples:
          list_of_parents.append(couple[0])
          list_of_parents.append(couple[1])
    
     my_dict = {i:list_of_parents.count(i) for i in list_of_parents}
     rec = sum([v for _, v in my_dict.items() if v > 1])
     print(f"Number of parents in >2 families: {round(rec/len(my_dict.keys())*100, 2)}")

def parents_with_2_families(people):
    
    couples = set()
    parents = set()
    rec = 0

    for _, person in people.items(): # O(x)
        
        if person.getParents()!=[]:
            
            p1, p2 = person.getParents()[0], person.getParents()[1]

            couples.add((p1, p2))
            parents.add(p1)
            parents.add(p2)

    num_parents = len(list(parents))
    encountered = set() # Records parents encountered twice. We do not want people who have children with 3 or more people to be included in rec more than once

    for couple in couples: # O(m)
        
        p1, p2 = couple[0], couple[1]
        
        if p1 not in parents and p1 not in encountered: # O(l)
            rec += 1
            encountered.add(p1) # Record that the parent has been encountered, and should not further contribute to the percentage
        if p2 not in parents and p2 not in encountered: # O(l)
            rec += 1
            encountered.add(p2)

        parents.discard(p1)
        parents.discard(p2)

    x = round(rec*100/num_parents)

    print(f"Percentage of people having children with 2 or more people: {x}%")


# Overall time complexity: O(m*(l+l)) = O(m*2*l) ~ O(m*l), where m is the number of couples found in the database and l is the number of 

##########################################################################

######################### Functions for exercise 12 #########################

def height_comparison_of_parents(people):
	"""Counting number of tall/tall, tall/normal, tall/short, normal/normal, 
	normal/short and short/short parent pairs"""
	
	tall_tall, tall_normal, tall_short, normal_normal, normal_short, short_short = 0, 0, 0, 0, 0, 0

	encountered_parents = list()

	for _, person in people.items():


		parents = person.getParents()


		if parents != [] and parents not in encountered_parents:

			#Making it so the father is always defined as p1
			if (int(people[parents[0]].getCPR()[9:11]) % 2) == 0:
				p1 = people[parents[1]]
				p2 = people[parents[0]]
			elif (int(people[parents[0]].getCPR()[9:11]) % 2) != 0:
				p1 = people[parents[0]]
				p2 = people[parents[1]]

			h1, h2 = int(p1.getHeight()), int(p2.getHeight())
			
			#Tall men
			if h1 > 184.4 and h2 > 170.2: tall_tall += 1                                #tall women
			elif h1 > 184.4 and h2 <= 170.2 and h2 >= 164.2: tall_normal += 1           #normal women
			elif h1 > 184.4 and h2 < 164.2: tall_short += 1                             #short women
			
			#Average men
			elif h1 <= 184.4 and h1 >= 178.4 and h2 > 170.2: tall_normal += 1                                #tall women
			elif h1 <= 184.4 and h1 >= 178.4 and h2 <= 170.2 and h2 >= 164.2: normal_normal += 1             #normal women
			elif h1 <= 184.4 and h1 >= 178.4 and h2 < 164.2: normal_short += 1                               #short women
			
			#Short men
			elif h1 < 178.4 and h2 > 170.2: tall_short += 1                             #tall women
			elif h1 < 178.4 and h2 <= 170.2 and h2 >= 164.2: normal_short += 1          #normal women
			elif h1 < 178.4 and h2 < 164.2: short_short += 1                            #short women

			encountered_parents.append(parents)

	total = tall_tall + tall_normal + tall_short + normal_normal + normal_short + short_short


	print("Heights\t\tPercentage" + "\nTall/tall\t"+str(round((tall_tall/total)*100, 2))+"%"+"\nTall/normal\t"+str(round((tall_normal/total)*100, 2))+"%"+"\nTall/short\t"+str(round((tall_short/total)*100, 2))+"%"+"\nNormal/normal\t"+str(round((normal_normal/total)*100, 2))+"%"+"\nNormal/short\t"+str(round((normal_short/total)*100,2))+"%"+"\nShort/short\t"+str(round((short_short/total)*100,2))+"%")

##########################################################################

######################### Functions for exercise 13 #########################

def children_heights(people):
	"""Function for finding the percentage of tall children with 2 tall parents"""
	girls, boys = [], []
	tall, normal, short = 0,0,0

	for _, person in people.items(): # O(x)

		parents = person.getParents()

		if parents != []:
			#Making it so the father is always defined as p1
			if (int(people[parents[0]].getCPR()[9:11]) % 2) == 0:
				p1 = people[parents[1]]
				p2 = people[parents[0]]
			elif (int(people[parents[0]].getCPR()[9:11]) % 2) != 0:
				p1 = people[parents[0]]
				p2 = people[parents[1]]

			#If both parenst are tall
			if p1.getHeight() > 184.4 and p2.getHeight() > 170.2:
				if (int(person.getCPR()[9:11]) % 2) == 0: girls.append(person.getHeight())                  #girls

				elif (int(person.getCPR()[9:11]) % 2) != 0: boys.append(person.getHeight())                 #boys

	for boy in boys: # O(b)
		if boy > 184.4: tall += 1
		elif boy <= 184.4 and boy >= 178.4: normal += 1
		if boy < 178.4: short += 1

	for girl in girls: # O(g)
		if girl > 170.2: tall += 1
		elif girl <= 170.2 and girl >= 164.2: normal += 1
		if girl < 164.2: short += 1

	total = tall + normal + short
	print("Height of child\tPercentage" + "\nTall\t"+str(round((tall/total)*100, 2))+"%" + "\nNormal\t"+str(round((normal/total)*100, 2))+"%" + "\nShort\t"+str((round((short/total)*100, 2)))+"%")
	print("According to the above distribution, it can be concluded that tall parents produce tall children.")

##########################################################################

######################### Functions for exercise 14 #########################

def BMI_of_parents(people):
	"""Counting number of fat/fat, fat/normal, fat/thin, normal/normal, 
	normal/thin and thin/thin parent pairs"""
	
	fat_fat, fat_normal, fat_thin, normal_normal, normal_thin, thin_thin = 0, 0, 0, 0, 0, 0

	encountered_parents = list() 

	for _, person in people.items(): # O(x)


		parents = person.Parents


		if parents != [] and parents not in encountered_parents: # O(l)

			p1 = people[parents[1]]
			p2 = people[parents[0]]


			h1, h2 = int(p1.getHeight()), int(p2.getHeight())
			w1, w2 = int(p1.getWeight()), int(p2.getWeight())
			p1_bmi, p2_bmi = w1/((h1/100)*(h1/100)), w2/((h2/100)*(h2/100))

			#fat men
			if p1_bmi > 25 and p2_bmi > 25: fat_fat += 1                                  #fat women
			elif p1_bmi > 25 and p2_bmi <= 25 and p2_bmi >= 18.5: fat_normal += 1         #normal women
			elif p1_bmi > 25 and p2_bmi < 18.5: fat_thin += 1                             #thin women
			
			#normal men
			elif p1_bmi <= 25 and p1_bmi >= 18.5 and p2_bmi > 25: fat_normal += 1                                    #fat women
			elif p1_bmi <= 25 and p1_bmi >= 18.5 and p2_bmi <= 25 and p2_bmi >= 18.5: normal_normal += 1             #normal women
			elif p1_bmi <= 25 and p1_bmi >= 18.5 and p2_bmi < 18.5: normal_thin += 1                                 #thin women
			
			#thin men
			elif p1_bmi < 18.5 and p2_bmi > 25: fat_thin += 1                                 #fat women
			elif p1_bmi < 18.5 and p2_bmi <= 25 and p2_bmi >= 18.5: normal_thin += 1          #normal women
			elif p1_bmi < 18.5 and p2_bmi < 18.5: thin_thin += 1                              #thin women

			encountered_parents.append(parents)

	total = fat_fat + fat_normal + fat_thin + normal_normal + normal_thin + thin_thin


	print("BMI:\t\tPercentage:" + "\nFat/fat\t\t"+str(round((fat_fat/total)*100, 2))+"%", "\nFat/normal\t"+str(round((fat_normal/total)*100, 2))+"%", "\nFat/thin\t"+str(round((fat_thin/total)*100, 2))+"%", "\nNormal/normal\t"+str(round((normal_normal/total)*100, 2))+"%", "\nNormal/thin\t"+str(round((normal_thin/total)*100, 2))+"%", "\nThin/thin\t"+str(round((thin_thin/total)*100, 2))+"%")				
	print("According to the above distribution, it is not obvious that people with higher BMIs have children at a significantly high rate.")


##########################################################################

######################### Functions for exercise 15 #########################

def not_biological_parent(people):
	"""Function for finding children whos listed parents are not their actual parents (at least 1 is not)"""
	inheritance = {("A", "A"): ("A", "O"), ("A","B"): ("A", "B", "AB", "O"), ("A", "AB"): ("A", "B", "AB"), ("A", "O"): ("A", "O"), ("B", "A"): ("A", "B", "AB", "O"), ("B", "B"): ("B", "O"), ("B", "AB"): ("A", "B", "AB"), ("B", "O"): ("B", "O"), ("AB", "A"): ("A", "B", "AB"), ("AB", "B"): ("A", "B", "AB"), ("AB", "AB"): ("A", "B", "AB"), ("AB", "O"): ("A", "B"), ("O", "A"): ("A", "O"), ("O", "B"): ("B", "O"), ("O", "AB"): ("A", "B"), ("O", "O"): ("O")}

	kids = []
	num_children = 0

	for _, person in people.items(): # O(x)

		parents = person.getParents()
		
		if parents != []:
			p1 = people[parents[0]]
			p2 = people[parents[1]]
			num_children+=1
			pbloodtype = (p2.getBloodType()[:-1], p1.getBloodType()[:-1])                 #Parents blood types, mother's first
			cbloodtype = person.getBloodType()[:-1]                                  #Person's blood type
			if cbloodtype not in inheritance[pbloodtype]: 
				kids.append(person.getCPR())

	s = "Children, where at least 1 parent is not their biological parent:\n"
	s += "\n".join(kids)
	print(s)
	print(f"{len(kids)} children have at least 1 non-biological parent.\nThis corresponds to {round(100*len(kids)/num_children, 2)}% of all children in the dataset")
	with open(r"data\kids-non-biological-parent.txt", "w+") as f:
		f.write(s)
     
##########################################################################

######################### Functions for exercise 16 #########################

def can_donate_to(bt1, bt2):
    x_can_donate_to = {"A+": ["A+", "AB+"], "A-": ["A+", "A-", "AB+", "AB-"], "B+":["B+", "AB+"], "B-":["B+","B-","AB+","AB-"], "O+": ["A+","B+","O+","AB+"], "O-": ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], "AB+":["AB+"], "AB-":["AB+", "AB-"]}
    return bt2 in x_can_donate_to[bt1]

def fathers_that_can_donate_blood_to_sons(people):
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
    
    father_cprs = [i for i,x in people.items() if x.getGender()=="Male" and len(x.getChildren())>0] # O(x))
    fToSDonate = {}

    for father_cpr in father_cprs: # O(l) ~ O(x)
        
        fToSDonate[father_cpr] = []
        father = people[father_cpr]
        
        for child_cpr in father.getChildren(): # O(c)
            
            child = people[child_cpr]
            
            if can_donate_to(father.getBloodType(), child.getBloodType()) and child.getGender()=="Male":
                fToSDonate[father_cpr].append(child_cpr)

    print("Father:\tSons that are able to recieve blood from father:")
    x = 0
    y = 0
    for father, sons in fToSDonate.items():
        if len(sons)>0:
            x+=1
            y += len(sons)
            print(f"{father}: {sons}")
    print(f"Total number of fathers that can donate blood to at least one son: {x}")
    print(f"Number of sons that can receive blood from their father: {y}")

##########################################################################

######################### Functions for exercise 17 #########################

def can_donate_to_grandparents(people):

    person_to_grandparents = {}

    for cpr, person in people.items(): # O(x)
        
        if person.getParents()!=[]:

            p1, p2 = people[person.getParents()[0]], people[person.getParents()[1]]
            l = []        
            l.extend(p1.getParents())            
            l.extend(p2.getParents())            
            person_to_grandparents[cpr] = l

    personToGrandparentsBlood = {}

    for person, grandparents in person_to_grandparents.items(): # O(x)
        
    
        x = [i for i in grandparents if can_donate_to(people[person].getBloodType(), people[i].getBloodType())] # O (g) ~ O(x)
        
        if x !=[]:
        
            personToGrandparentsBlood[person] = x

    s = ""
    print("Person:\tGrandparents that can recieve their blood:")
    for person, grandparents in personToGrandparentsBlood.items():
         s += f"{person}: {grandparents}\n"

    print(s)
    print(f"Total number of grandchildren: {len(personToGrandparentsBlood.keys())}")
    print(f"Total number of grandparents: {sum([len(i) for i in personToGrandparentsBlood.values()])}")

##########################################################################
