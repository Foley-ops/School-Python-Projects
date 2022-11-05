import csv


def print_stat():
    if initial_loan == 0:
        print(f'Initial loan amount: ${loan_token:.2f}')
        print(f'Loan term is: {years} years and {months} months')
        print(f'Total amount paid: ${total_monthly_payments:.2f}')
        print(f'Total interest paid: ${monthly_interest_c:.2f}')
    elif initial_loan != 0:
        print(f'Initial loan amount: ${loan_token:.2f}')
        print(f'Total amount paid: ${total_monthly_payments:.2f}')
        print(f'Loan amount leftover: ${amount_leftover:.2f}')
        print(f'Total interest paid: ${monthly_interest_c:.2f}')


def writer():
    loan_writer.writerow(
        [f'{month_count}', f'{initial_loan:.2f}', f'{monthly_interest_c:.2f}',
         f'{total_monthly_payments:.2f}'])


month_count = 0
monthly_interest_c = 0
total_monthly_payments = 0


x = input('Enter desired file name: ')
initial_loan = loan_token = float(input('What is the amount of the loan? '))
percent_apr = float(input('What is your APR? '))
monthly_payment = float(input('How much will you pay per month? '))

actual_apr = percent_apr / 100
monthly_interest = (loan_token * actual_apr) / 12
total_monthly_payments += monthly_payment
total_cost_token = loan_token + (loan_token * actual_apr)

row2 = [month_count, f'{initial_loan:.2f}',
        f'{0}', f'{0}']
loan_file = open(f'{x}.csv', 'w', newline='')
fieldnames = ('Month', 'Loan Amount', 'Interest Accrued', 'Amount Paid')
loan_writer = csv.writer(loan_file)
loan_writer.writerow(fieldnames)
loan_writer.writerow(row2)


loan_and_apr = initial_loan + monthly_interest
after_payment = loan_and_apr - monthly_payment


if initial_loan <= after_payment:

    for i in range(0, 30):
        month_count += 1

        if month_count == 1:
            total_monthly_payments = monthly_payment
            monthly_interest_c = monthly_interest
        else:
            total_monthly_payments += monthly_payment
            monthly_interest_c += monthly_interest

        initial_loan = (initial_loan - monthly_payment) + monthly_interest
        amount_leftover = initial_loan
        writer()

else:
    while 0 < initial_loan:
        month_count += 1

        if month_count == 1:
            total_monthly_payments = monthly_payment
            monthly_interest_c = monthly_interest
        else:
            total_monthly_payments += monthly_payment
            monthly_interest_c += monthly_interest

        initial_loan = (initial_loan - monthly_payment) + monthly_interest

        writer()

        if initial_loan < monthly_payment:
            month_count += 1
            monthly_payment = initial_loan
            total_monthly_payments += monthly_payment
            initial_loan -= monthly_payment
            writer()
years = month_count // 12
months = month_count % 12

print_stat()

loan_file.close()
