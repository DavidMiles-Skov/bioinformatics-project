#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 14:
A BMI below 18.5 is considered thin, 18.5-25 normal, and 25+ overweight (fat)

Notes:
Directory needs to be fixed
"""

def BMI_of_parents(people):
	"""Counting number of fat/fat, fat/normal, fat/thin, normal/normal, 
	normal/thin and thin/thin parent pairs"""
	
	fat_fat, fat_normal, fat_thin, normal_normal, normal_thin, thin_thin = 0, 0, 0, 0, 0, 0

	encountered_parents = list()

	for cpr, person in people.items():


		parents = person.getParents()


		if person.getParents() != [] and parents not in encountered_parents:

			p1, p2 = people[person.getParents()[0]], people[person.getParents()[1]]

			p1_bmi, p2_bmi = p1.getBMI(), p2.getBMI()

			#fat 1st parent
			if p1_bmi > 25 and p2_bmi > 25: fat_fat += 1                                  #fat
			elif p1_bmi > 25 and p2_bmi <= 25 and p2_bmi >= 18.5: fat_normal += 1         #normal
			elif p1_bmi > 25 and p2_bmi < 18.5: fat_thin += 1                             #thin
			
			#normal 1st parent
			elif p1_bmi <= 25 and p1_bmi >= 18.5 and p2_bmi > 25: fat_normal += 1                                    #fat
			elif p1_bmi <= 25 and p1_bmi >= 18.5 and p2_bmi <= 25 and p2_bmi >= 18.5: normal_normal += 1             #normal
			elif p1_bmi <= 25 and p1_bmi >= 18.5 and p2_bmi < 18.5: normal_thin += 1                                 #thin
			
			#thin 1st parent
			elif p1_bmi < 18.5 and p2_bmi > 25: fat_thin += 1                                 #fat
			elif p1_bmi < 18.5 and p2_bmi <= 25 and p2_bmi >= 18.5: normal_thin += 1          #normal
			elif p1_bmi < 18.5 and p2_bmi < 18.5: thin_thin += 1                              #thin

			encountered_parents.append(parents)

	total = fat_fat + fat_normal + fat_thin + normal_normal + normal_thin + thin_thin


	print("BMI\t\tPercentage" + "\nFat/fat\t\t"+str((fat_fat/total)*100)+"%", "\nFat/normal\t"+str((fat_normal/total)*100)+"%", "\nFat/thin\t"+str((fat_thin/total)*100)+"%", "\nNormal/normal\t"+str((normal_normal/total)*100)+"%", "\nNormal/thin\t"+str((normal_thin/total)*100)+"%", "\nThin/thin\t"+str((thin_thin/total)*100)+"%")				

def main():
	people = getData()
	BMI_of_parents(people)

if __name__ == "__main__":
	main()
