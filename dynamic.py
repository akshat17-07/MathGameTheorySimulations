import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime


# this are the local variables that would store the results of each run
result = []


"""
This is the main function of the program and it runs the whole simulations.
Problem: Dynamic probablity changing
"""
def main():

    # taking the inputs
    num = int(input("enter number of resturants: "))
    decrease = int(input("enter percentage decrease: "))
    days = int(input("how many days do you want to run the program: "))
    increase = decrease / num

    # creating dataframe that stores probablity of all agents and resturants
    data = []
    for i in range(num):
        data.append([])
        for j in range(num):
            data[i].append(100)

    df = pd.DataFrame(data, columns = range(1, num+1))

    for i in range(days):
        # this function would convert all negative number into positive numbers
        df = check_negative(df)
        df = run(df, decrease, increase, num)

    plt.plot(result)
    title = "kolkata Paise dynamic Problem with days = " + str(days) + " and number of resturnts = " + str(num) + " decrease by " + str(decrease)

    plt.title(title)

    plt.xlabel("Number of days")

    plt.show()




"""
This is a helper function and it convert all negative probablity into the positive ones and returns the modified dataframe
"""
def check_negative(df):
    df[df <0 ] = 0
    return df

"""
This is a helper function and it runs the simulations for one day and returns the modified dataframe
"""
def run(df, decrease, increase, num):

    # finding the sum of all df rows
    sum = df.sum()
    index = 0
    repeat = 0
    selected = []

    for i in sum:
        # finding the resturant agent will chose
        temp = random.uniform(0, i)
        value = 0
        col = 0
        for j in df.loc[index]:
            value += j
            if value >= temp:
                break
            col += 1

        if (col + 1) > num:

            col -= 1

        # changing the agent matrix
        df.loc[index]+= increase
        df.loc[index, col+ 1] -= decrease

        # checking if the resturant is already selected
        if col in selected:
            repeat += 1
        else:
            selected.append(col)

        # appending the agent
        index += 1

    # adding the repeat to the list
    result.append((num - repeat) * 100 / num)
    return df






if __name__ == "__main__":
    main()
