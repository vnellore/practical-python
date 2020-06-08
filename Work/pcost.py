# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):

    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)
        total_cost = 0.0
        for line in rows:
            print(line)
            try:
                name, shares, price = line
                total_cost += float(shares) * float(price)
            except Exception:
                print('Exception occurred')  
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost {cost}')
