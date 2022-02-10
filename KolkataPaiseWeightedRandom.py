import simpy
import random


def randomselection(env):

    """
    this function weighted random selection algorithm
    """

    # asking for number of resturant
    numberOfResturants = int(input("enter the number of resturants/ hotels: "))
    avg = 0

    # creting a weighted resturant list
    weighted = []
    for i in range(1,numberOfResturants+1):
        weighted += [i]*i # appending i j times


    while True:
        resturantWithoutAgents = 0

        # reseting resturnts
        resturants = resetResturantselection(numberOfResturants)

        # randomly assigning agents to resturant
        for i in range(numberOfResturants):
            resturants[random.choice(weighted)] = 1

        # checking resturant without agents
        for i in resturants:
            if not resturants[i]:
                resturantWithoutAgents += 1

        # new avg = ( (cur avg * 99) + (resturantWithoutAgents/numberOfResturants) ) / 100
        avg = ((avg*env.now)+(resturantWithoutAgents/numberOfResturants))/(env.now + 1)

        print(env.now + 1, "run gives", resturantWithoutAgents, "without agents")
        print("avg of agents who get food is after this run is", (1 - avg)*100)

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

    env.process(randomselection(env))

    env.run(until=int(input("how many days program should run: ")))
