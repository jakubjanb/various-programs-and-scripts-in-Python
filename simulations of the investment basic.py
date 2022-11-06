# This program allows you to simulate the behaviour of a long-term investment with a variable rate of return.
# We conduct 10,000 simulations lasting ten years with interest counted yearly. We take the annual investment
# income from a random selection from the normal distribution with a certain average and standard deviation.

import random
from matplotlib.pyplot import hist, show


# a function, “ChangeInBalance,” takes in the current balance as
# a parameter and returns how much it changes 1 year later.
def ChangeInBalance(initial_balance):
    # pick a random rate of return each year from the normal distribution,
    # where first value is mean percentage of income and the second value is the standard deviation
    # if you would like to use uniform distribution in some range of values we use rate = random.uniform(-0.03,0.07)

    rate = random.gauss(0.06, 0.04)
    return initial_balance * rate


# here we define for how many years the investment last 'number_years', and
# how many simulations we want to perform 'number_sims'
# we collect all the data in the list 'final_balances'
number_years = 10
number_sims = 10000
final_balances = []
for i in range(number_sims):
    # Set initial conditions
    time = 0
    balance = 1000

    while time < number_years:
        # Increase balance and time
        balance += ChangeInBalance(balance)
        time += 1

    final_balances.append(balance)

# Output the simulation results
# for i in range(number_sims):
# print("Final Balance:", final_balances[i])

hist(final_balances, bins=20)
show()
