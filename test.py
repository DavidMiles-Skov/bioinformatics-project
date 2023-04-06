from person import Person
from read_data import getData
from read_data import addParents

def main():

    people = getData()

    # Checking if adding parents worked

    people_with_parents = addParents(people)

    print("260195-4304 and 081295-4166 should both have parents: 281267-6456 and 220567-1489")
    print(people_with_parents["260195-4304"])
    print(people_with_parents["081295-4166"])



if __name__=="__main__":

    main()


