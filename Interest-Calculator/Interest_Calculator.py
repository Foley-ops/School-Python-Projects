import csv

# function for all statements
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

# function for writer in column format
def writer():
    loan_writer.writerow(
        [f'{month_count}', f'{initial_loan:.2f}', f'{monthly_interest_c:.2f}',
         f'{total_monthly_payments:.2f}'])

# zeroed values for use in calculations
month_count = 0
monthly_interest_c = 0
total_monthly_payments = 0

# inputs for file name, loan amounts, apr, and monthly payment
x = input('Enter desired file name: ')
initial_loan = loan_token = float(input('What is the amount of the loan? '))
percent_apr = float(input('What is your APR? '))
monthly_payment = float(input('How much will you pay per month? '))

# calculations that create the variables to be used
# apr is converted from percent to decimal value
actual_apr = percent_apr / 100
# monthly intest is calculated by * loan amount and apr
# then devided by twelve to get monthly interest
monthly_interest = (loan_token * actual_apr) / 12
total_monthly_payments += monthly_payment
total_cost_token = loan_token + (loan_token * actual_apr)

# row2 makes the second row print out with zeroed out interest and total payment
row2 = [month_count, f'{initial_loan:.2f}',
        f'{0}', f'{0}']
loan_file = open(f'{x}.csv', 'w', newline='')
# feildnames gives csv file a header
fieldnames = ('Month', 'Loan Amount', 'Interest Accrued', 'Amount Paid')
loan_writer = csv.writer(loan_file)
loan_writer.writerow(fieldnames)
loan_writer.writerow(row2)


# this formula allows us to calculate if loan can be paid off eventually
# by adding intrest and total loan, and subtracting by the monthly payment
loan_and_apr = (initial_loan + monthly_interest) -  monthly_payment

# if loan cannot be paid off then we run this for loop
# which shows how much interest accures over 30 months
if initial_loan <= loan_and_apr:

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
# writer() adds values to csv
# If loan can be paid off then we calculate how long, how much interest, and how much was paid.        
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
# writer() adds values to csv
        writer()
# this if statement calculates the very last line in the csv file so it zeros out
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
# always close file
