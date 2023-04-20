#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 6:
- Count number of females, who do not have children
- Count number of males, who do not have children
- Divide them respectively with the total amount of female/male and multiply with 100%

"""

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

def main():
	people = getData()
	Parenthood_percentage()

if __name__ == "__main()__":
	main()
