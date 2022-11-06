import random
import statistics
from matplotlib.pyplot import hist, show

# 'historical_sp500' list contains historical annual returns on investments in the largest US stock index,
# the S&P500 from the last 77 years
historical_sp500 = [-.22, .2871, .1840, .3149, -.0438, .2183, .1196, .0138, .1369, .3239, .16, .0211, .1506, .2646,
                    -.37, .0549, .1579, .0491, .1088, .2868, -.2210, -.1189, -.0910, .2104, .2858,
                    .3336, .2296, .3758, .0132, .1008, .0762, .3047, -.0310, .3169, .1661, .0525, .1867, .3173, .0627,
                    .2256, .2155, -.0491, .3242, .1844, .0656, -.0718, .2384, .3720, -.2647,
                    -.1466, .1898, .1431, .0401, -.0850, .1106, .2398, -.1006, .1245, .1648, .2280, -.0873, .2689,
                    .0047, .1196, .4336, -.1078, .0656, .3156, .5262, -.0099, .1837, .2402, .3171, .1879, .055,
                    .0571, -.0807]

# historical_ten_year_bonds is a list of annual returns from ten-year bonds in US, list contains data from 60 years,
# starting from year 2022 to the past
historical_ten_year_bonds = [.0281, .0145, .0089, 0.0214, .0291, .0233, .0184, .0214, .0254, .0235, .018,
                             .0278, .0322, .0326, .0366, .0463, .048, .0429, .0427, .0401, .0461, .0502, .0603,
                             .0565, .0526, .0635, .0644, .0657, .0709, .0587, .0701, .0786, .0855, .0849, .0885,
                             .0839, .0767, .1062, .1246, .1110, .1301, .1392, .1143, .0943, .0841, .0742, .0761,
                             .0799, .0756, .0685, .0621, .0616, .0735, .0667, .0564, .0507, .0493, .0428, .0419, .04]


def ChangeInBalanceStocks(initial_balance):
    # here we randomly select an element from the 'historical_sp500'
    # list as an annual interest rate for the investment based on the stock market
    rate = random.choice(historical_sp500)
    return initial_balance * rate


def ChangeInBalanceBonds(initial_balance):
    # here we randomly select an element from the 'historical_ten_year_bonds'
    # list as an annual interest rate for the investment based on ten years bonds
    rate = random.choice(historical_ten_year_bonds)
    return initial_balance * rate


# here we define for how many years the investment last 'number_years', and
# how many simulations we want to perform 'number_sims'
# we collect all the data in the list 'final_balances'
number_years = 10
number_sims = 10000
final_balances_stocks = []
final_balances_bonds = []

for i in range(number_sims):
    # Set initial conditions
    time = 0
    balance_stocks = 1000
    balance_bonds = 1000

    while time < number_years:
        # Increase balance and time
        balance_stocks += ChangeInBalanceStocks(balance_stocks)
        balance_bonds += ChangeInBalanceBonds(balance_bonds)
        time += 1

    final_balances_stocks.append(balance_stocks)
    final_balances_bonds.append(balance_bonds)

# statistical information computed from the results of the simulation

final_balances_average_stocks = statistics.mean(final_balances_stocks)
final_balances_standard_deviation_stocks = statistics.stdev(final_balances_stocks)
print("The final average balance for S&P500 investment is:", final_balances_average_stocks)
print("The standard deviation in the final balance for S&P500 is:", final_balances_standard_deviation_stocks)
final_balances_average_bonds = statistics.mean(final_balances_bonds)
final_balances_standard_deviation_bonds = statistics.stdev(final_balances_bonds)
print("The final average balance for bonds investment is:", final_balances_average_bonds)
print("The standard deviation in the final balance for bonds is:", final_balances_standard_deviation_bonds)

# Visualisation of the result
# Here on one histogram we plot data from two simulations
# We can see investment in stock is more risky, but may give much higher profit
hist([final_balances_stocks, final_balances_bonds], bins=20)
show()
