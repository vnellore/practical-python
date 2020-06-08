# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)

        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception:
                pass

    return prices


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

initial_portfolio_value = 0.0
current_portfolio_value = 0.0
for holding in portfolio:
    name, shares, price = holding['name'], holding['shares'], holding['price']
    initial_portfolio_value += shares * price
    current_portfolio_value += prices[name] * shares


print(f'Initial portfolio value is {initial_portfolio_value}')
print(f'Current portfolio value is {current_portfolio_value}')

print(f'Net gain is {current_portfolio_value - initial_portfolio_value}')
