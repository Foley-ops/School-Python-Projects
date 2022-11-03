import csv

month_count = 0
monthly_interest_c = 0
total_monthly_payments = 0

x = 'test'
initial_loan = 10_000
percent_apr = 2.75
monthly_payment = 1_000

# x = input('Enter desired file name: ')
# initial_loan = float(input('What is the amount of the loan? '))
# percent_apr = float(input('What is your APR? '))
# monthly_payment = float(input('How much will you pay per month? '))

actual_apr = percent_apr / 100
amount_after = initial_loan - monthly_payment
monthly_interest = (amount_after * actual_apr) / 12
remaining_amount = amount_after + monthly_interest
total_monthly_payments += monthly_payment

row2 = [month_count, f'{initial_loan:.2f}', f'{monthly_interest:.2f}', f'{total_monthly_payments:.2f}']
# print(f'Amount paid :{total_monthly_payment:.2f}')
# print(f'monthly interest :{monthly_interest:.2f}')
# print(f'remaining amount :{remaining_amount:.2f}')

loan_file = open(f'{x}.csv', 'w')
fieldnames = ('Month', 'Loan Amount', 'Interest', 'Amount Paid')
loan_writer = csv.writer(loan_file)
loan_writer.writerow(fieldnames)
loan_writer.writerow(row2)


test_1 = monthly_interest * 30
test_2 = monthly_payment * 30
test_3 = initial_loan - (test_1 + test_2)

loan_amount_c = initial_loan


if 0 < test_3:
    for i in range(0, 30):
        month_count += 1
        initial_loan = (initial_loan - monthly_payment) + monthly_interest
        total_monthly_payments += monthly_payment
        monthly_interest_c += monthly_interest
        loan_writer.writerow(
            [f'{month_count}', f'{initial_loan:.2f}', f'{monthly_interest_c:.2f}', f'{total_monthly_payments:.2f}'])

elif test_3 <= 0:
    while 0 <= remaining_amount:
        month_count += 1
        remaining_amount -= (monthly_payment + monthly_interest)
        initial_loan = ((initial_loan - monthly_payment) + monthly_interest)
        total_monthly_payments += monthly_payment
        monthly_interest_c += monthly_interest
        loan_writer.writerow(
            [f'{month_count}', f'{initial_loan:.2f}', f'{monthly_interest_c:.2f}',
             f'{total_monthly_payments:.2f}'])

else:
    print('trash')

loan_file.close()
