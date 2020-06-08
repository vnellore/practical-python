# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month \
     and month <= extra_payment_end_month:
        adjusted_payment = payment + extra_payment
    else:
        adjusted_payment = payment

    if adjusted_payment > principal:
        adjusted_payment = principal
        principal = 0

    total_paid = total_paid + adjusted_payment

    if principal > 0:
        principal = principal * (1 + rate / 12) - adjusted_payment
    print(f'{month} {total_paid:0.2f} {principal:0.2f}')
    month += 1
