# report.py
#
# Exercise 2.12

import csv
import sys

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        portfolio = []
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                portfolio.append({'name' : record['name'], 'shares' : int(record['shares']), 'price' : float(record['price'])})
            except ValueError:
                print(f'Could not line {rowno}, bad line: {row}')
                continue
    return portfolio


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue
    return prices


def report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for item in portfolio:
        if item['price'] >= prices[item['name']]:
            price_change = (item['price'] - prices[item['name']]) * -1
        else:
            price_change = prices[item['name']] - item['price']

        report.append((item['name'], item['shares'], item['price'], price_change))

    return report


def print_report(report_data):
    '''
    Print report from the report_data list of tuples containing (name, shares, price, change).
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report_data:
        print(f'{name:>10} {shares:>10} {format("${:.2f}".format(price)):>10} {change:>10.2f}')
    return


if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = '/home/nhershberger/Code/practical-python/Work/Data/portfolio.csv'
    prices_filename = '/home/nhershberger/Code/practical-python/Work/Data/prices.csv'

report = report_data(read_portfolio(portfolio_filename), read_prices(prices_filename))
print_report(report)