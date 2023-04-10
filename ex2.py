from person import Person
from read_data import getData
import matplotlib.pyplot as plt
from collections import Counter




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
            print(person.CPR)
            yFather = int(person.CPR[4:6])
            print(yFather)
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yFather)
    ages.sort()
    counter = Counter(ages)
    for number, count in counter.items():
        print(f"{number}: {count}")
    

def main():
    d = getData()
    firstTimeFatherAge(d)


if __name__=="__main__":
    main()




                
