from read_data import getData

def calcParentAgeDiff(people):
    
    encountered_children = set()
    differences = []
    
    for cpr, person in people.items():
        

        parents = person.Parents


        if parents != [] and cpr not in encountered_children:
        
            p1 = people[parents[0]]
            p2 = people[parents[1]]
            diff = abs(int(p1.CPR[4:6])-int(p2.CPR[4:6]))
            differences.append(diff)

            # Making sure that mother/father pair are not added to list again

            for child in p1.Children:
                encountered_children.add(child)


    print(f"Average age differences between parents in data: {round(sum(differences)/len(differences))}")

def main():
    people = getData()
    calcParentAgeDiff(people)

if __name__ == "__main__":
    main()