import random
import matplotlib.pyplot as plt

def run():

    # taking the inputs
    days = int(input("How many days is simulation running: "))
    groups = []

    # creting the groups for the simulation
    print("Enter the number of agent in the group.\n You could create as many groups as u want and to enter 0.\n If this is you do not wish to enter more groups enter 0.")
    num_agent = 1
    while True:
        i = int(input("size: "))
        if (i == 0):
            break
        dict = {}
        for j in range(i):
            dict[num_agent] = 0
            num_agent += 1

        groups.append(dict)

    # checking if the groups exist or not
    if len(groups) == 0:
        print("Enter atleast one group")
        return 0

    # creating free agents
    free_agent = int(input("number of free agent: "))
    dict = {}
    for i in range(free_agent):
        dict[num_agent] = 0
        num_agent += 1
    free_agent = dict

    # asking for number of resturants
    no_of_resturants = int(input("number of resturants: "))

    # checking if everything is legit
    for i in groups:
        if len(i) > no_of_resturants:
            print("group size could not be greater than number of resturants")
            return 1

    # running simulation
    for i in range(days):

        # agents choicing resturants
        dict_rest = CreateResturantsDict(no_of_resturants)

        # running simulating in for groups chosing resturant
        for agent in groups:
            list_rest = list(range(1,no_of_resturants + 1))
            for k in agent:
                temp = random.choice(list_rest)
                list_rest.remove(temp)
                dict_rest[temp].append(k)

        # running simulation on free agent chocing resturant
        list_rest = list(range(1,no_of_resturants + 1))
        for k in free_agent:
            temp = random.choice(list_rest)
            dict_rest[temp].append(k)

        # calculating the results
        for j in dict_rest:
            if len(dict_rest[j]) != 0:
                temp = random.choice(dict_rest[j])
                if temp in free_agent:
                    free_agent[temp] += 1

                else:
                    for g in groups:
                        if temp in g:
                            g[temp] += 1
                            break
    print("groups:")
    for g in groups:
        print(g)

    print("free agents:")
    print(free_agent)

    return 0


"""
This cerate resturants dicts
"""
def CreateResturantsDict(i):
    dict = {}
    for j in range(i):
        dict[j+1] = []

    return dict

if __name__ == "__main__":
    run()
