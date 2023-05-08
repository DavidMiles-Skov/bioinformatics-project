from read_data import getData
import matplotlib.pyplot as plt
from collections import Counter




def calcAveFirstTimeFatherAge(persondict):
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
    x = 31.3 # Average age of first-time fathers in denmark according to statistics denmark
    print("--------------Comparison of mean age of first-time fatherhood----------------")
    print(f"Test data: {round(sum(ages)/len(ages), 1)}\nData from Statistics Denmark: {x}")



def main():
    d = getData()
    calcAveFirstTimeFatherAge(d)


if __name__=="__main__":
    main()




                
