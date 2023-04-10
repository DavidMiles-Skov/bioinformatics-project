#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 6:

- Count number of females, who do not have children
- Count number of males, who do not have children
- Divide them respectively with the total amount of female/male and multiply with 100%

Notes:
Is there much point in using a function for this exercise? 
Only neccesary object is the dict from the "getData" function, which auto selects "people.db"
Rest is simply itterating over the dict.values, which are all of the "person" class, and so we use the methods of that class (.Gender and .Children)
Seems to me it makes more sense for the "getData" function to be changed to accept any given data file 
I suppose i'll leave this as a function for the time being
"""

def Parenthood_percentage():                          #Needs to be updated to the proper path, this was just made from own directory
	"""Percentage of males and females who are not parents"""
	males, females = [], []
	people = getData()


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

#print(Parenthood_percentage())