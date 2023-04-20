#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 14:
A BMI below 18.5 is considered thin, 18.5-25 normal, and 25+ overweight (fat)

Notes:
Output code wise is a bit yikes, not very familiar with string formatting, perhaps you have a better solution
Directory needs to be fixed
The BMI calculation could be added as a method for the person class,
that way we could skip it here, should be simple since every person has a weight and height already
"""

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

def main:
	people = getData()
	BMI_of_parents(people)

if __name__ == "__main()__":
	main()
