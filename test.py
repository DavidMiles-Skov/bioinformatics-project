from person import Person
from read_data import getData
from read_data import addParents

def main():

    people = getData()

    # Checking if adding parents worked
    for cpr, person in people.items():
        if len(person.Parents)==1:
            print("!")




if __name__=="__main__":

    main()


