import random
import csv

def run(times, days, groups, free_agent, no_of_resturants):
    data =[]


    for i in range(len(groups) + 1):
        data.append([])

    # running simulation
    for t in range(times):
        # running simulation for 1 time
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

        # calculating mean
        for grp in groups:
            for g in grp.keys():
                grp[g] = grp[g]*100/days

        for f in free_agent.keys():
            free_agent[f] = free_agent[f]*100/days

        for g in range(len(groups)):
            data[g].append(len(groups[g]))

        data[-1].append(len(free_agent))

        (groups, free_agent) = resuffle(groups, free_agent)

    for d in data:
        print(d)


    return data

"""
this function resuffles groups and free agents
"""
def resuffle(groups, free_agent):
    avg = {}

    group_no = 0

    removed_agents = {}

    for grp in groups:
        avg[group_no] = sum(grp.values())/len(grp)


        new_group = {}

        for g in grp.keys():
            if grp[g] >= avg[group_no]:
                new_group[g] = 0

            else:
                removed_agents[g] = 0

        groups[group_no] = new_group
        group_no += 1

    for f in free_agent.keys():
        temp = []

        for i in range(len(avg)):
            if free_agent[f] > avg[i]:
                temp.append(i)

        if len(temp) == 0:
            removed_agents[f] = 0

        else:
            selected = random.choice(temp)
            groups[selected][f] = 0

    """
    print("groups: after suffling ")
    for g in groups:
        print(g)

    print("agents after suffling")
    print(removed_agents)
    """
    return (groups, removed_agents)

"""
This cerate resturants dicts
"""
def CreateResturantsDict(i):
    dict = {}
    for j in range(i):
        dict[j+1] = []

    return dict

def createCsv(data, run, name):
    name += "run_"
    name += str(run)

    with open(name, 'w') as f:
        writer = csv.writer(f)

        header = []
        for d in range(1,len(data)+1):
            header.append("Groups " + str(d))

        header[-1] = "free agent"

        writer.writerow(header)

        rows = []
        for d in data[0]:
            rows.append([])

        for da in data:
            for d in range(len(da)):
                rows[d].append(da[d])

        for r in rows:
            writer.writerow(r)

def inputs():
    # taking the inputs
    times = int(input("How many times is simulation running: "))
    days = int(input("How many days is simulation running before we sort groups: "))
    runs = int(input("How many runs do you want to have: "))
    name = input("name floder you want to see data in: ")
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

    for x in range(1, runs+1):

        print("run", x)
        g = []

        for i in groups:
            g.append(i.copy())
        f = free_agent.copy()

        data = run(times, days, g, f, no_of_resturants)
        createCsv(data, x, name)

        print("\n---------------------------\n---------------------------\n")


if __name__ == "__main__":
    inputs()
