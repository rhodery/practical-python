# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        headers = next(lines)

        total_cost = 0.00
        for lineno, line in enumerate(lines, start=1):
            record = dict(zip(headers, line))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print(f'Line {lineno}: Bad row: {line}')
                continue

        #f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '/home/nhershberger/Code/practical-python/Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')