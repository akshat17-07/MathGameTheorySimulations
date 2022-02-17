import simpy
import random
import matplotlib.pyplot as plt

day = [] # global variable day would store the number of days
data = [] # global varialble data woudl store the data points

def randomselection(env, numberOfResturants):

    """
    this function random selection algorithm
    """


    # defining queue
    maxQueue = int(input("enter the maximum number of people that could be in queue: "))

    avg = 0

    while True:
        resturantWithoutAgents = 0

        # reseting resturnts
        resturants = resetResturantselection(numberOfResturants)

        # randomly assigning agents to resturant
        for i in range(numberOfResturants):
            flag = True
            while flag:

                temp = random.randint(1,numberOfResturants)

                if len(resturants[temp]) < maxQueue:

                    flag = False
                    resturants[temp].append(i)



        # checking resturant without agents
        for i in resturants:
            if resturants[i] == []:
                resturantWithoutAgents += 1

        avg = ((avg*env.now)+(resturantWithoutAgents/numberOfResturants))/(env.now + 1)

        day.append(env.now+1)
        data.append((1-avg)*100)

        yield env.timeout(1)


def resetResturantselection(numberOfResturants):
    """
    this funciton return the dict of with empty list
    """
    resturants = {}

    # creating an empty list of resturants
    for i in range(numberOfResturants):
        resturants[i+1] = []

    return resturants

if __name__ == "__main__":
    env = simpy.Environment()

    # asking for number of resturant
    numberOfResturants = int(input("enter the number of resturants/ hotels: "))

    env.process(randomselection(env, numberOfResturants))

    time = int(input("how many days program should run: "))

    env.run(until=time)

    plt.plot(day, data)
    title = "kolkata Paise Queue Problem with days = " + str(time) + " and number of resturnts = " + str(numberOfResturants)

    plt.title(title)

    plt.xlabel("Number of days")

    plt.show()
