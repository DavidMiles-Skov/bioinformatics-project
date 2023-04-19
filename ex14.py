#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 14:
A BMI below 18.5 is considered thin, 18.5-25 normal, and 25+ overweight (fat)

Notes:
havent made the "main()" formatting
output needs to be cleaned up so you can tell what percentage is what
Directory needs to be fixed
"""

def BMI_of_parents():
	"""Counting number of fat/fat, fat/normal, fat/thin, normal/normal, 
	normal/thin and thin/thin parent pairs"""
	
	fat_fat, fat_normal, fat_thin, normal_normal, normal_thin, thin_thin = 0, 0, 0, 0, 0, 0
	
	people = getData()

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


	return str((fat_fat/total)*100), (fat_normal/total)*100, (fat_thin/total)*100, (normal_normal/total)*100, (normal_thin/total)*100, (thin_thin/total)*100				

#print(BMI_of_parents())
