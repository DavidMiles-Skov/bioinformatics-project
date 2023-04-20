#!/usr/bin/env python3

"""
Attempting to solve exercise 15:
Using the inheritance chart from https://canadiancrc.com/paternity_determination_blood_type.aspx 

Notes:
As far as i could read the rhesus +/- system is inherited seperately from the ABO-system, so I've only based it on the ABO-system
Directory needs fixing
Output needs fixing

"""

from read_data import getData

def not_the_parents():
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

	return kids

def main():
	people = getData()
	not_the_parents(people)

if __name__ == "__main()__":
	main()
