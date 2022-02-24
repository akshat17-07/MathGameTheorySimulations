import simpy
import random
import matplotlib.pyplot as plt

day = [] # global variable day would store the number of days
data = [] # global varialble data woudl store the data points


def randomselection(env, numberOfResturants):

    """
    this function random selection algorithm
    """
    avg = 0

    while True:
        resturantWithoutAgents = 0

        # reseting resturnts
        resturants = resetResturantselection(numberOfResturants)

        # randomly assigning agents to resturant
        for i in range(numberOfResturants):
            resturants[random.randint(1,numberOfResturants)] = 1

        # checking resturant without agents
        for i in resturants:
            if not resturants[i]:
                resturantWithoutAgents += 1

        # new avg = ( (cur avg * 99) + (resturantWithoutAgents/numberOfResturants) ) / 100
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
        resturants[i+1] = None

    return resturants

if __name__ == "__main__":
    env = simpy.Environment()

    # asking for number of days program should run
    time = int(input("how many days program should run: "))
    # asking for number of resturant
    numberOfResturants = int(input("enter the number of resturants/ hotels: "))

    env.process(randomselection(env, numberOfResturants))


    env.run(until=time)


    plt.plot(day, data)
    title = "kolkata Paise Random selection Problem with days = " + str(time) + " and number of resturnts = " + str(numberOfResturants)

    plt.title(title)

    plt.xlabel("Number of days")

    plt.show()
