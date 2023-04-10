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
            yFather = int(person.CPR[4:6])
            # Finding the eldest child
            eldest = min([int(x[4:6]) for x in person.Children])
            ages.append(eldest-yFather)
    ages.sort()
    counter = Counter(ages)
    age_vals = [i for i in counter.keys()]
    prop = [i/len(ages) for i in counter.values()]
    plt.bar(age_vals, prop)
    plt.xlabel("Age of first-time fatherhood")
    plt.ylabel("Proportion")
    plt.title("Distribution of ages of first-time fatherhood")
    plt.show()

def main():
    d = getData()
    firstTimeFatherAge(d)


if __name__=="__main__":
    main()




                
