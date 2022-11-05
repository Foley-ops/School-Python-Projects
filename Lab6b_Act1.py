
# main dict where everything is stored
user_pass = {}
# two supplemental working lists specifically for the print statement
un = []
pw = []

count = 0
quest = str(input('Would you like to create an account?(Yes/No)'))

if quest == 'Yes' or quest == 'YES' or quest == 'yes' or quest == 'y' or quest == 'Y':
    quest = True

if quest is True:
    num = int(input('How many accounts?'))

    while num < 1:
        print('Please enter a positive number')
        num = int(input('How many accounts?'))

    while quest is True and count != num:
        count += 1

        add_user = input("Please enter desired username:")
        un.append(add_user)
        add_pass = input("Please enter desired password:")
        pw.append(add_pass)
        verif_pass = input("Please verify password")

        # password verifier to help user remember password
        while add_pass != verif_pass:
            print('Passwords do not match! Please try again!')
            verif_pass = input("Please verify password")

        user_pass[add_user] = add_pass
    # first print statement to help assist with remembering password entered

    if count == 1:
        print(count, 'account created.')
    elif count >= 1:
        print(count, 'accounts created.')
    print('Username list:')
    print(*un, sep="\n")
    print('Password list:')
    print(*pw, sep="\n")

    # log in using any username password combo
    print('Time to log in!')
    username = input('Please enter your username:')
    password = input('Please enter your password:')

    if user_pass.get(username) == password:
        # print username and passwords as requested in prompt
        print('You have successfully logged in!')

    # loop so user has chance to reenter incorrect username or password
    elif user_pass.get(username) != password:
        while user_pass.get(username) != password:
            print('Invalid username or password!')
            print('Please try again!')
            username = input('Please enter your username:')
            password = input('Please enter your password:')

            if user_pass.get(username) == password:
                # print username and passwords as requested in prompt
                print('You have successfully logged in!')

# Alternate ending if user does not wish to make account
else:
    print('Have a nice day!')
