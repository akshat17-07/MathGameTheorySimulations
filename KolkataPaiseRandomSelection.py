"""
    Problem : Kolkata Paise Resturant
    Variant: Random Selection
"""

import random
import simpy

class Agent:

    # defining agent
    def __init__(self, evn, number):
        self.history = []

    # adding agent history
    def addHistory(self, f):
        self.history.append(f)



class setup:
    def __init__(self, numberOfDays, evn, agent, resturant, numberOfResturants):
        self.numberOfDays = numberOfDays
        self.evn = evn
        self.agent = agent
        self.resturant = resturant
        self.num = numberOfResturants
        self.history = 0

    def runSimulation(self):

        for i in range(1, 1 + self.num):

            evn.process(self.process())

            yield self.evn.Timeout(1)

        evn.run()
        self.history = self.history/numberOfDays

        print("on avg", self.history, "resturant did not get agents")
        self.history = 0



    def process(self):
        yield request


        resturantWithoutAgents = 0

        # selecting agents selecting the resturant
        for a in self.agents:
            resturant[random(self.num)].append(a)

        for r in self.resturant:
             # checking if multiple agents are at resturant
             if self.resturant[r] != []:
                 self.resturant[r] = []

             else:
                resturantWithoutAgents += 1

        print("on day", self.evn.now(), "their were", resturantWithoutAgents ,"resturant did not get agents")

        self.history += resturantWithoutAgents




if "__main__" == __name__:
    agent = {}
    resturant = {}

    # calculation number of resturant
    numberOfResturants = int(input("Enter number of agent/Resturant: "))

    env = simpy.Environment()

    # creating agents and resturant
    for i in range(1, 1 + numberOfResturants):
        agent[i+1] = Agent(env, i)
        resturant[i+1] = []

    # taking number of time simulation must run
    numberOfDays = int(input("Enter number of days simulation is to run: "))

    setup = setup(numberOfDays, env, agent, resturant, numberOfResturants)

    setup.runSimulation()
