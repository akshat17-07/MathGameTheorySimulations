import random
import matplotlib.pyplot as plt

"""
This is my custom variation of kolkata Paisa problem
In this variation the agent would not repeat a restrant once he went to it until he had tried all of the resturants
"""
def run ():
    # defining the starting variables
    num_agent = int(input("enter number of agents: "))
    runs = int(input("enter the amount of days program should run: "))
    dict_resturants = {}
    dict_agent = {}
    withoutAgent = 0
    days = [] # x - axis
    result = [] # y - axis

    # creating intial dicts for agents and resturants
    for i in range(1, num_agent + 1):
        dict_agent[i] = intialList(num_agent)
        dict_resturants[i] = []

    # running simulations
    for i in range(runs):
        for j in dict_agent.keys():

            # reassigning the list if it is empty
            if dict_agent[j] == []:
                dict_agent[j] = intialList(num_agent)

            temp = random.choice(dict_agent[j]) # chosing random resturants
            dict_resturants[temp].append(j) # appending agent in the list of resturants

        for j in dict_resturants.keys():

            # finding if the resturant is empty or nto
            if dict_resturants[j] == []:
                withoutAgent += 1

            else:
                # removing resturant from list of agent that eaten at the resturant
                temp = random.choice(dict_resturants[j])
                dict_agent[temp].remove(j)

        # reassigning dict resturants
        dict_resturants = resetDictResturants(num_agent)
        outcome = (num_agent - withoutAgent)*100/num_agent
        withoutAgent = 0
        days.append(i)
        result.append(outcome)

    # ploting the graph
    plt.plot(days, result)
    title = "kolkata Paise No Repeat Problem with days = " + str(len(days)) + " and number of resturnts = " + str(num_agent)

    plt.title(title)
    plt.ylabel("result")
    plt.xlabel("Number of days")

    plt.show()


"""
This function would reset dict resturants
"""
def resetDictResturants(num):
    dict = {}
    for i in range(1, num+1):
        dict[i] = []

    return dict



"""
This function would make a initial dict of agents on a resturant
"""
def intialList(num):
    l = []
    for n in range(1, num+1):
        l.append(n)
    return l





if __name__ == "__main__":
    run()
