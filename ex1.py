from read_data import getData

"""
Attempting to solve exercise 1.

- Will use dictionary to store age ranges as shown on project webpage.
- The same will be done with danish population data.
- The two will be compared.
"""

def addAgeToDict(age, target_dict, amount=1):
    if age>=16 and age<=20:
        target_dict["16-20"]+=amount
    elif age>=21 and age<=25:
        target_dict["21-25"]+=amount
    elif age>=26 and age<=30:
        target_dict["26-30"]+=amount
    elif age>=31 and age<=35:
        target_dict["31-35"]+=amount
    elif age>=36 and age<=40:
        target_dict["36-40"]+=amount
    elif age>=41 and age<=45:
        target_dict["41-45"]+=amount
    else:
        target_dict["46+"]+=amount
    return target_dict
    
    
def calcAgeDistDKData(filepath=r"data\DKpopulation.csv"):
    data = open(filepath, "r")
    male_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }
    female_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }
    data = data.readlines()[1:]
    for line in data:
        l = line.split(";")
        age = int(l[1].split()[0])
        gender = l[2]
        amount=int(l[-1])
        
        if gender=="Men": addAgeToDict(age, male_ages, amount=amount)
        elif gender=="Women": addAgeToDict(age, female_ages, amount=amount)
        else: raise Exception("Error in determining gender")

    total_male = sum(male_ages.values())
    total_female = sum(female_ages.values())

    # Converting from numbers to percentages

    male_prop = {agerange: round((num/total_male)*100,2) for agerange, num in male_ages.items()}
    female_prop = {agerange: round((num/total_female)*100, 2) for agerange, num in female_ages.items()}
    
    return male_prop, female_prop
    



def calcAgeDistTest(people):
    """
    Calculates the age distribution of the test data
    
    """
    male_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }
    female_ages = {"16-20": 0,
                "21-25": 0,
                "26-30": 0,
                "31-35": 0,
                "36-40": 0,
                "41-45": 0,
                "46+": 0 }

    for cpr, person in zip(people.keys(), people.values()):
        age = 100-int(cpr[4:6])

        if person.Gender=="Male": male_ages = addAgeToDict(age, male_ages)
        else: female_ages = addAgeToDict(age, female_ages)
    
    total_male = sum(male_ages.values())
    total_female = sum(female_ages.values())

    # Converting from numbers to percentages

    male_prop = {agerange: round((num/total_male)*100,2) for agerange, num in male_ages.items()}
    female_prop = {agerange: round((num/total_female)*100, 2) for agerange, num in female_ages.items()}
    
    return male_prop, female_prop
        




def main():

    people = getData(r"data\people.db")

    m_ages_test, f_ages_test = calcAgeDistTest(people)

    m_ages_data, f_ages_data = calcAgeDistDKData()

    print("------Comparing age distributions------")
    print("Distribution of ages from \"people.db\":")
    
    for ages in m_ages_test.keys():
        print(f"{ages}:\nMale: {m_ages_test[ages]}%\nFemale: {f_ages_test[ages]}%\n")
    
    print("Distribution of ages from \"DKpopulation.csv\":")

    for ages in m_ages_test.keys():
        print(f"{ages}:\nMale: {m_ages_data[ages]}%\nFemale: {f_ages_data[ages]}%\n")
    
    


if __name__=="__main__":
    main()
