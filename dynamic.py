
import random
import matplotlib.pyplot as plt

"""
This is the main function that runs the problem
in this problem we would assign problity of selecting a resturant as for all agent as a constant number at first but then as agent will select a resturant problity of going back to that resturant would decrease by 10% whereas probablity of selecting another resturant would increase by 10%/n times
"""

def dynamic():
    # x axis
    days = []
    # y axis
    result = []

    # asking for the initial conditions
    num_of_resturants = int(input("enter no of resturants: "))
    probablity_dict = createDict(num_of_resturants)
    percentage = int(input("enter percentage the probablity of going to the resturant twice should decrease by: "))
    decrease = num_of_resturants * percentage / 100
    increase = decrease/num_of_resturants
    runs = int(input("number of times you want to run this program: "))
    total_probablity = num_of_resturants * 1000
    avg = 0

    # runing the case
    for i in range(runs):
        resturantsWithoutAgents = 0
        resturant_taken = set()

        for agent in probablity_dict.keys():
            random = randomSelection(probablity_dict[agent], total_probablity)

            if random in resturant_taken:
                resturantsWithoutAgents += 1
            else:
                resturant_taken.add(random)

            probablity_dict[agent] = newProbablityDict(probablity_dict[agent], random, decrease, increase)
        avg += (num_of_resturants - resturantsWithoutAgents)*100/num_of_resturants
        days.append(i)
        result.append((num_of_resturants - resturantsWithoutAgents)*100/num_of_resturants)


    print(avg/runs)
    plt.plot(days, result)
    title = "kolkata Paise Dynamic Selection Problem with days = " + str(days[-1]) + " and number of resturnts = " + str(num_of_resturants) + "decrease % = " + str(percentage) + "%"

    plt.title(title)
    plt.ylabel("result")
    plt.xlabel("Number of days")

    plt.show()


"""
This function would create and return a new problaty matrix for a agent
"""
def newProbablityDict(dict, random, decrease, increase):
    for i in dict.keys():
        dict[i] += increase
        if i == random:
            dict[i] -= decrease

    return dict



"""
This function would select a resturant randomly from the list of resturants
"""
def randomSelection(dict, total_probablity):
    select = random.uniform(0, total_probablity)

    for i in dict.keys():
        select -= dict[i]
        if select <= 0:
            return i




"""
This function would create a dict of the resturants
"""
def createDict(num):
    dict = {}
    l = {}

    # creating a list of probablity
    for i in range(num):
        l[i+1] = 1000

    for i in range(1,num+1):
        dict[i] = l

    return dict



if __name__ == "__main__":
    dynamic()
