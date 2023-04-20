#!/usr/bin/env python3

from read_data import getData

"""
Attempting to solve exercise 12:
Average height for men = 181,4 +- 3 cm
Average height for women = 167,2 +- 3 cm
Tall and short are above and below those limits respectively

Notes;
Using some of the same coding from ex7
directory needs fixing to github direct
Extra note:
It seems like the somewhat randomization of the dataset has made the average height of women a lot higher than whats typical,
So maybe there should not be any differentiation between men and women in terms of what is consiudered tall
This also explains why there are such few normal/normal couples, as the amount of normal height women is very low
"""

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


	print("Heights\t\tPercentage" + "\nTall/tall\t"+str((tall_tall/total)*100)+"%", "\nTall/normal\t"+str((tall_normal/total)*100), "\nTall/short\t"+str((tall_short/total)*100), "\nNormal/normal\t"+str((normal_normal/total)*100), "\nNormal/short\t"+str((normal_short/total)*100), "\nShort/short\t"+str((short_short/total)*100))			

def main():
	people = getData()
	height_comparison_of_parents(people)

if __name__ == "__main()__":
	main()
