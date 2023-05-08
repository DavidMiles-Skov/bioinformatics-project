#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 13
Tall is considered above 184.4 cm for men and above 170.2 for women
Notes:
Output formatting code-wise is a bit, yeah, not to familiar with formatting for strings, perhaps you have a better solution
Same as in ex12, Ive realied the height for women on average is very tall compared to denmark statistics
Maybe we should not differentiate between them in that case

"""

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

def main():
	people = getData()
	children_heights(people)

if __name__ == "__main__":
	main()
