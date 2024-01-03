# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = float(input('Interest rate: '))
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = float(input('Extra payment: '))
extra_payment_start_month = float(input('Extra payment start month: '))
extra_payment_end_month = float(input('Extra payment end month: '))

while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        new_payment = payment + extra_payment
    else:
        new_payment = payment

    if principal < new_payment:
        new_payment = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - new_payment
    
    total_paid = total_paid + new_payment

    output_data = f'Month: {month}, total paid: {total_paid:0.2f}, remaining principal: {principal:0.2f}'
    print(output_data)

print('Total paid:', round(total_paid, 2), 'Months:', month)