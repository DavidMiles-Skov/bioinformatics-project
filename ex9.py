from read_data import getData


def findAveCousins(dict):
    """
    - Takes dictionary of cpr->person and returns average number of cousins (float)
    - Cousins are found via:
        - Initialise empty set to keep track of traversed parents/uncles/aunts
        - For each person in the dictionary (grandparents)
            - if grandparents not considered:
                - add grandparents to set
                - Initialise sum = 0 (sum represents number of cousins in current family)
                - For every child of that person (parents/uncles/aunts)
                    - sum += number of children for current child 
                - append sum to list 
        - return average of list
    """

    num_cousins = []
    considered_grandparents = set()

    for cpr,grandparent in dict.items():
        if grandparent.Children !=[] and cpr not in considered_grandparents: # Person has children and family has not already been considered
            # Finding person's partner
            c1 = dict[grandparent.Children[0]]
            partner = [i for i in c1.Parents if i != cpr][0]
            # Adding grandparents to set
            considered_grandparents.add(cpr)
            considered_grandparents.add(partner)
            parent_cprs = grandparent.Children
            cousins = 0
            for p_cpr in parent_cprs: # iterating through parents 
                cousins += len(dict[p_cpr].Children) # Summing up number of cousings
            num_cousins.append(cousins)
    return f"Average number of cousins: {sum(num_cousins)/len(num_cousins)}"


def main():
    people = getData()
    print(findAveCousins(people))


if __name__=="__main__":
    main()