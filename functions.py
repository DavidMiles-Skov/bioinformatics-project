from read_data import *
import matplotlib.pyplot as plt
from collections import Counter




######################## Functions for exercise 1 ########################

def addAgeToDict(age, target_dict, amount=1):
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
        
def calcAgeDistDKData(filepath=r"data\DKpopulation.csv"):
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
        
        if gender=="Men": addAgeToDict(age, male_ages, amount=amount)
        elif gender=="Women": addAgeToDict(age, female_ages, amount=amount)
        else: raise Exception("Error in determining gender")

    total_male = sum(male_ages.values())
    total_female = sum(female_ages.values())

    # Converting from numbers to percentages

    male_prop = {agerange: round((num/total_male)*100,2) for agerange, num in male_ages.items()}
    female_prop = {agerange: round((num/total_female)*100, 2) for agerange, num in female_ages.items()}
    
    return male_prop, female_prop
    
def calcAgeDistTest(people):
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

    for cpr, person in zip(people.keys(), people.values()):
        age = 100-int(cpr[4:6])

        if person.Gender=="Male": male_ages = addAgeToDict(age, male_ages)
        else: female_ages = addAgeToDict(age, female_ages)
    
    total_male = sum(male_ages.values())
    total_female = sum(female_ages.values())

    # Converting from numbers to percentages

    male_prop = {agerange: round((num/total_male)*100,2) for agerange, num in male_ages.items()}
    female_prop = {agerange: round((num/total_female)*100, 2) for agerange, num in female_ages.items()}
    
    return male_prop, female_prop


# Final function 

def ageAndGenderDist(people):
    
    m_ages_test, f_ages_test = calcAgeDistTest(people)
    m_ages_data, f_ages_data = calcAgeDistDKData()

    print("------Comparing age and gender distributions------")
    print("Age range:\nGender:\npeople.db\tDKpopulation.csv:\n")
    
    for ages in m_ages_test.keys():
        print(f"{ages}:\nM: {m_ages_test[ages]}%\t{m_ages_data[ages]}%\nF: {f_ages_test[ages]}%\t{f_ages_data[ages]}")

########################################################################


######################## Functions for exercise 2 ########################

def firstTimeFatherAge(persondict):
    """
    Will calculate the age at which fathers have their first child.
    - Father: XXXXFF-XXXX
    - Child: XXXXCC-XXXX
    - Age at fatherhood: CC-FF
    """
    ages = []

    for person in persondict.values():
        if person.Children != [] and person.Gender=="Male":
            yFather = int(person.CPR[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yFather)
    ages.sort()
    counter = Counter(ages)
    age_vals = [i for i in counter.keys()]
    prop = [i/len(ages) for i in counter.values()]
    plt.bar(age_vals, prop)
    plt.xlabel("Age of first-time fatherhood")
    plt.ylabel("Proportion")
    plt.title("Distribution of ages of first-time fatherhood")
    plt.show()

##########################################################################

######################## Functions for exercise 3 ########################

def calcAveFirstTimeFatherAge(persondict):
    """
    Will calculate the average age at which fathers have their first child.
    - Father: XXXXFF-XXXX
    - Child: XXXXCC-XXXX
    - Age at fatherhood: CC-FF
    """
    ages = []

    for person in persondict.values():
        if person.Children != [] and person.Gender=="Male":
            yFather = int(person.CPR[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yFather)
    x = 31.3 # Average age of first-time fathers in denmark according to statistics denmark
    print("--------------Comparison of mean age of first-time fatherhood----------------")
    print(f"Test data: {round(sum(ages)/len(ages), 1)}\nData from Statistics Denmark: {x}")

##########################################################################

######################## Functions for exercise 4 ########################

def firstTimeMotherAge(persondict):
    """
    Will calculate the age at which Mothers have their first child.
    - Father: XXXXFF-XXXX
    - Child: XXXXCC-XXXX
    - Age at fatherhood: CC-FF
    """
    ages = []

    for person in persondict.values():
        if person.Children != [] and person.Gender=="Female":
            yFather = int(person.CPR[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yFather)
    ages.sort()
    counter = Counter(ages)
    age_vals = [i for i in counter.keys()]
    prop = [i/len(ages) for i in counter.values()]
    plt.bar(age_vals, prop)
    plt.xlabel("Age of first-time motherhood")
    plt.ylabel("Proportion")
    plt.title("Distribution of ages of first-time motherhood")
    plt.show()

##########################################################################

######################## Functions for exercise 5 ########################

def calcAveFirstTimeMotherAge(persondict):
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
    print("--------------Comparison of mean age of first-time fatherhood----------------")
    print(f"Test data: {round(sum(ages)/len(ages), 1)}\nData from Statistics Denmark (2006): {x}")

##########################################################################

######################## Functions for exercise 6 ########################

def Parenthood_percentage(people):                          #Needs to be updated to the proper path, this was just made from own directory
	"""Percentage of males and females who are not parents"""
	males, females = [], []


	for person in people.values():                                                                 #Iterating over the person class values in the getData dict
		#"1" means they have children, "0" means they do not have children
		if person.Gender == "Male" and len(person.Children) != 0: males.append("1")          
		elif person.Gender == "Male" and len(person.Children) == 0: males.append("0")
		if person.Gender == "Female" and len(person.Children) != 0: females.append("1")
		elif person.Gender == "Female" and len(person.Children) == 0: females.append("0")


	Number_of_males = len(males)
	Number_of_females = len(females)


	Non_fathers = males.count("0")
	Non_mothers = females.count("0")

	return "Percentage of non fathers: " + str((Non_fathers/Number_of_males)*100), "percentage of non mothers: " + str((Non_mothers/Number_of_females)*100)


##########################################################################

######################## Functions for exercise 7 ########################

def calcParentAgeDiff(people):
    
    encountered_children = set()
    differences = []
    
    for cpr, person in people.items():
        

        parents = person.Parents


        if parents != [] and cpr not in encountered_children:
        
            p1 = people[parents[0]]
            p2 = people[parents[1]]
            diff = abs(int(p1.CPR[4:6])-int(p2.CPR[4:6]))
            differences.append(diff)

            # Making sure that mother/father pair are not added to list again

            for child in p1.Children:
                encountered_children.add(child)


    print(f"Average age differences between parents in data: {round(sum(differences)/len(differences))}")

##########################################################################

######################## Functions for exercise 8 ########################

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

##########################################################################

######################## Functions for exercise 9 ########################

def findAveCousins(dict):
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

    for cpr,grandparent in dict.items():
        if grandparent.Children !=[] and cpr not in considered_grandparents: # Person has children and family has not already been considered
            # Finding person's partner
            c1 = dict[grandparent.Children[0]]
            partner = [i for i in c1.Parents if i != cpr][0]
            # Adding grandparents to set
            considered_grandparents.add(cpr)
            considered_grandparents.add(partner)
            parent_cprs = grandparent.Children
            cousins = 0
            for p_cpr in parent_cprs: # iterating through parents 
                cousins += len(dict[p_cpr].Children) # Summing up number of cousings
            num_cousins.append(cousins)
    return f"Average number of cousins: {sum(num_cousins)/len(num_cousins)}"

##########################################################################

######################### Functions for exercise 10 #########################

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

##########################################################################

######################### Functions for exercise 11 #########################

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

##########################################################################

######################### Functions for exercise 12 #########################

def height_comparison_of_parents(people):
	"""Counting number of tall/tall, tall/normal, tall/short, normal/normal, 
	normal/short and short/short parent pairs"""
	
	tall_tall, tall_normal, tall_short, normal_normal, normal_short, short_short = 0, 0, 0, 0, 0, 0

	encountered_parents = list()

	for cpr, person in people.items():


		parents = person.Parents


		if parents != [] and parents not in encountered_parents:

			#Making it so the father is always defined as p1
			if (int(people[parents[0]].CPR[9:11]) % 2) == 0:
				p1 = people[parents[1]]
				p2 = people[parents[0]]
			elif (int(people[parents[0]].CPR[9:11]) % 2) != 0:
				p1 = people[parents[0]]
				p2 = people[parents[1]]

			h1, h2 = int(p1.Height), int(p2.Height)
			
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


	print("Heights\t\tPercentage" + "\nTall/tall\t"+str((tall_tall/total)*100)+"%", "\nTall/normal\t"+str((tall_normal/total)*100)+"%", "\nTall/short\t"+str((tall_short/total)*100)+"%", "\nNormal/normal\t"+str((normal_normal/total)*100)+"%", "\nNormal/short\t"+str((normal_short/total)*100)+"%", "\nShort/short\t"+str((short_short/total)*100)+"%")			

##########################################################################

######################### Functions for exercise 13 #########################

def children_heights(people):
	"""Function for finding the percentage of tall children with 2 tall parents"""
	girls, boys = [], []
	tall, normal, short = 0,0,0

	for cpr, person in people.items():

		parents = person.Parents

		if parents != []:
			#Making it so the father is always defined as p1
			if (int(people[parents[0]].CPR[9:11]) % 2) == 0:
				p1 = people[parents[1]]
				p2 = people[parents[0]]
			elif (int(people[parents[0]].CPR[9:11]) % 2) != 0:
				p1 = people[parents[0]]
				p2 = people[parents[1]]

			#If both parenst are tall
			if p1.Height > 184.4 and p2.Height > 170.2:
				if (int(person.CPR[9:11]) % 2) == 0: girls.append(person.Height)                  #girls

				elif (int(person.CPR[9:11]) % 2) != 0: boys.append(person.Height)                 #boys

	for boy in boys:
		if boy > 184.4: tall += 1
		elif boy <= 184.4 and boy >= 178.4: normal += 1
		if boy < 178.4: short += 1

	for girl in girls:
		if girl > 170.2: tall += 1
		elif girl <= 170.2 and girl >= 164.2: normal += 1
		if girl < 164.2: short += 1

	total = tall + normal + short
	print("Height\tPercentage" + "\nTall\t"+str((tall/total)*100)+"%" + "\nNormal\t"+str((normal/total)*100)+"%" + "\nShort\t"+str((short/total)*100)+"%")


##########################################################################

######################### Functions for exercise 14 #########################

def BMI_of_parents(people):
	"""Counting number of fat/fat, fat/normal, fat/thin, normal/normal, 
	normal/thin and thin/thin parent pairs"""
	
	fat_fat, fat_normal, fat_thin, normal_normal, normal_thin, thin_thin = 0, 0, 0, 0, 0, 0

	encountered_parents = list()

	for cpr, person in people.items():


		parents = person.Parents


		if parents != [] and parents not in encountered_parents:

			p1 = people[parents[1]]
			p2 = people[parents[0]]


			h1, h2 = int(p1.Height), int(p2.Height)
			w1, w2 = int(p1.Weight), int(p2.Weight)
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


	print("BMI\t\tPercentage" + "\nFat/fat\t\t"+str((fat_fat/total)*100)+"%", "\nFat/normal\t"+str((fat_normal/total)*100)+"%", "\nFat/thin\t"+str((fat_thin/total)*100)+"%", "\nNormal/normal\t"+str((normal_normal/total)*100)+"%", "\nNormal/thin\t"+str((normal_thin/total)*100)+"%", "\nThin/thin\t"+str((thin_thin/total)*100)+"%")				


##########################################################################

######################### Functions for exercise 15 #########################

def not_the_parents(people):
	"""Function for finding children whos listed parents are not their actual parents (at least 1 is not)"""
	inheritance = {("A", "A"): ("A", "O"), ("A","B"): ("A", "B", "AB", "O"), ("A", "AB"): ("A", "B", "AB"), ("A", "O"): ("A", "O"), ("B", "A"): ("A", "B", "AB", "O"), ("B", "B"): ("B", "O"), ("B", "AB"): ("A", "B", "AB"), ("B", "O"): ("B", "O"), ("AB", "A"): ("A", "B", "AB"), ("AB", "B"): ("A", "B", "AB"), ("AB", "AB"): ("A", "B", "AB"), ("AB", "O"): ("A", "B"), ("O", "A"): ("A", "O"), ("O", "B"): ("B", "O"), ("O", "AB"): ("A", "B"), ("O", "O"): ("O")}

	kids = []

	for cpr, person in people.items():

		parents = person.Parents
		
		if parents != []:
			p1 = people[parents[0]]
			p2 = people[parents[1]]

			pbloodtype = (p2.BloodType[:-1], p1.BloodType[:-1])                 #Parents blood types, mother's first
			cbloodtype = person.BloodType[:-1]                                  #Person's blood type
			if cbloodtype not in inheritance[pbloodtype]:
				kids.append(person)

	print("Children, where at least 1 parent is not their biological parent:\n")
	print(kids)

##########################################################################

######################### Functions for exercise 16 #########################

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

##########################################################################

######################### Functions for exercise 17 #########################

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

##########################################################################
