"""
This function run the problem with group of the fixed size that the user defines at the start
"""
import random
import matplotlib.pyplot as plt
result = []

def run():
    days = int(input("How many days is simulation running: "))
    groups = []
    print("Enter the number of agent in the group.\n You could create as many groups as u want and to enter 0.\n If this is you do not wish to enter more groups enter 0.")
    while True:
        i = int(input("size: "))
        if (i == 0):
            break
        groups.append(i)

    if len(groups) == 0:
        print("Enter atleast one group")
        return 0

    free_agents = int(input("Enter Number of free agents: "))

    total_agents = 0
    for i in groups:
        total_agents += i

    total_agents += free_agents

    for d in range(days):
        avg = 0
        dinning = []

        for i in groups:
            temp = list(range(total_agents))
            for j in range(i):
                t = random.choice(tuple(temp))
                temp.remove(t)

                if t in dinning:
                    avg += 1

                else:
                    dinning.append(t)

        temp = range(total_agents)
        for i in range(free_agents):
            t = random.choice(tuple(temp))
            if t in dinning:
                avg += 1

            else:
                dinning.append(t)

        result.append((total_agents - avg)*100/total_agents)

    plt.plot(result)

    plt.ylabel("result")
    plt.xlabel("Number of days")

    total = 0
    for i in result:
        total += i
    avg = total/ len(result)
    print("avg", avg)
    plt.show()


if "__main__" == __name__:
    run()
