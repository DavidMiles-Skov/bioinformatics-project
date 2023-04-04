from person import Person
from read_data import getData

def main():

    people = getData()

    # Checking if adding parents worked

    print(people["091070-8366"])

if __name__=="__main__":

    main()


