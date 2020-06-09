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
            holding = {'name': row[0], 'shares': int(row[1]),
                       'price': float(row[2])}
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


def make_report(portfolio, prices):
    report = []
    for x in portfolio:
        row = (x['name'], x['shares'], prices[x['name']],
               prices[x['name']] - x['price'])
        report.append(row)
    headers = ('Name', 'Shares', 'Price', 'Change')

    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('%10s %10s %10s %10s' % ('-' * 10, '-' * 10, '-' * 10, '-' * 10))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
make_report(portfolio, prices)
