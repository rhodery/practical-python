# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    lines = csv.reader(f)
    # skip headers
    next(f)

    total_cost = 0.00
    for lineno, line in enumerate(lines):
        try:
            shares = float(line[1])
            price = float(line[2])
            total_cost = total_cost + (shares * price)
        except ValueError:
            print(f'Could not process file data on line {lineno}: {line}')
            continue

    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '/home/nhershberger/Code/practical-python/Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')