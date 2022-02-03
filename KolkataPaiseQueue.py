import simpy
import random


def randomselection(env):

    """
    this function random selection algorithm
    """

    # asking for number of resturant
    numberOfResturants = int(input("enter the number of resturants/ hotels: "))

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
        resturants[i+1] = []

    return resturants

if __name__ == "__main__":
    env = simpy.Environment()

    env.process(randomselection(env))

    env.run(until=int(input("how many days program should run: ")))
