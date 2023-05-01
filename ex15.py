#!/usr/bin/env python3

"""
Attempting to solve exercise 15:
Using the inheritance chart from https://canadiancrc.com/paternity_determination_blood_type.aspx 

Notes:
Directory needs fixing
Output can be improved

"""

from read_data import getData

def not_the_parents(people):
	"""Function for finding children whos listed parents are not their actual parents (at least 1 is not)"""
	inheritance = {("A", "A"): ("A", "O"), ("A","B"): ("A", "B", "AB", "O"), ("A", "AB"): ("A", "B", "AB"), ("A", "O"): ("A", "O"), ("B", "A"): ("A", "B", "AB", "O"), ("B", "B"): ("B", "O"), ("B", "AB"): ("A", "B", "AB"), ("B", "O"): ("B", "O"), ("AB", "A"): ("A", "B", "AB"), ("AB", "B"): ("A", "B", "AB"), ("AB", "AB"): ("A", "B", "AB"), ("AB", "O"): ("A", "B"), ("O", "A"): ("A", "O"), ("O", "B"): ("B", "O"), ("O", "AB"): ("A", "B"), ("O", "O"): ("O")}

	kids = []

	for cpr, person in people.items():

		if person.getParents() != []:
			p1, p2 = people[person.getParents()[0]], people[person.getParents()[1]]
			

			pbloodtype = (p1.getBloodType()[:-1], p2.getBloodType()[:-1])                 #Parents blood types
			cbloodtype = person.getBloodType()[:-1]                                       #Person's blood type
			if cbloodtype not in inheritance[pbloodtype]:
				kids.append(person)

	print("Children, where at least 1 parent is not their biological parent:\n")
	print(kids)

def main():
	people = getData()
	not_the_parents(people)

if __name__ == "__main__":
	main()
