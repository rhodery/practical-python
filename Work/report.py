# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)

        portfolio = []
        for row in rows:
            try:
                portfolio.append({'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])})
            except ValueError:
                print(f'Could not process file data: {row}')
                continue
    return portfolio


def read_prices(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue
    return prices


def calc_gain_loss(portfolio, prices):
    total_cost = 0.0
    total_value = 0.0
    for item in portfolio:
        total_cost += item['shares'] * item['price']
        total_value += item['shares'] * prices[item['name']]
    
    if total_cost >= total_value:
        gain_loss = (total_cost - total_value) * -1
    else:
        gain_loss - total_value - total_cost
    return total_cost, total_value, gain_loss


if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = '/home/nhershberger/Code/practical-python/Work/Data/portfolio.csv'
    prices_filename = '/home/nhershberger/Code/practical-python/Work/Data/prices.csv'

cost, value, gain_loss = calc_gain_loss(read_portfolio(portfolio_filename), read_prices(prices_filename))
print(f'Total cost: {cost:0.2f}')
print(f'Total value: {value:0.2f}')
print(f'Gain/loss: {gain_loss:0.2f}')