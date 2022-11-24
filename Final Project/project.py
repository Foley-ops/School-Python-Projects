import random

scoring_test = []

def rules():
    print("*****RULES*****\n1. Two to nine players can play\n"
          "2. Each player rolls dice up to three times but can stop at one or two\n"
          "3. If the player before you rolled less than three time, you have to match their roll number\n ")


# rules()


def game_type():
    print("There are three different game types: Standard, Simple Scoring, and Alternate Chip Distribution.")
    more_info = int(input("Do you want more info?\n"
                          "0 - I don't need any more info!\n"
                          "1 - Standard Rules\n"
                          "2 - Simple Scoring Rules\n"
                          "3 - Alternate Chip Distribution\n"
                          "Type the indicated number for the desired option: "))

    if more_info == 0:
        pass # goto standard game
    elif more_info == 1:
        print("B")
    elif more_info == 2:
        print("This variant is the same as regular Zanzibar except\n"
              "the sum of combinations are only their face value.\n"
              "Ones and sixes are only worth 1 point and 6 points\n"
              "respectively, instead of 100 points and 60 points.")
    elif more_info == 3:
        print("This variant is the same as regular Zanzibar\n"
              "except the losing player receives a number of\n"
              "chips from each other player based on each\n"
              "player's score instead of just the winner's score")
    else:  # this might be better as a while statement, while more_info != 0,1,2,3
        print("Sorry I don't recognize that input.\nPlease try again")

    # quest = input("What game type do you want to play?")

# game_type()


def player_names(x):
    p_names = []
    for i in range(x):
        p_name = input(f"Please enter player {i + 1} name: ")
        p_names.append(p_name)

    print('Players are:\n', end=' * ')
    [print(i, end=' * ') for i in p_names]
    print()


p_amount = int(input("How many people will be playing? "))

# player_names(p_amount)

player_score = []

# creates amount of lists based on number of players
# score is set to whatever
for i in range(p_amount):
    player_score.append(20)
print(player_score)





# set_player()


def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    print(roll1, ',', roll2, ',', roll3)
    return roll1, roll2, roll3


def roll_score(roll1, roll2, roll3):
    '''
    Differentiates scores
    :param roll1: First die
    :param roll2: Second die
    :param roll3: Third die
    :return: score
    '''
    turn_score = 0
    if (roll1 == 4 or roll1 == 5 or roll1 == 6) and (roll2 == 4 or roll2 == 5 or roll2 == 6) and \
            (roll3 == 4 or roll3 == 5 or roll3 == 6) and roll1 != roll2 and roll2 != roll3 and roll1 != roll3:
        print('Zanzibar!')
        turn_score += 1000

    elif roll1 == roll2 == roll3:
        print('Three of a kind!')
        turn_score += 800

    elif (roll1 == 1 or roll1 == 2 or roll1 == 3) and (roll2 == 1 or roll2 == 2 or roll2 == 3) and \
            (roll3 == 1 or roll3 == 2 or roll3 == 3) and roll1 != roll2 and roll2 != roll3 and roll1 != roll3:
        print('123!')
        turn_score += 500

    if turn_score <= 0:

        if roll1 == 1:
            turn_score += 100

        if roll2 == 1:
            turn_score += 100

        if roll3 == 1:
            turn_score += 100

        if roll1 == 6:
            turn_score += 60

        if roll2 == 6:
            turn_score += 60

        if roll3 == 6:
            turn_score += 60

        if roll1 == 2:
            turn_score += 2

        if roll2 == 2:
            turn_score += 2

        if roll3 == 2:
            turn_score += 2

        if roll1 == 3:
            turn_score += 3

        if roll2 == 3:
            turn_score += 3

        if roll3 == 3:
            turn_score += 3

        if roll1 == 4:
            turn_score += 4

        if roll2 == 4:
            turn_score += 4

        if roll3 == 4:
            turn_score += 4

        if roll1 == 5:
            turn_score += 5

        if roll2 == 5:
            turn_score += 5

        if roll3 == 5:
            turn_score += 5

    if turn_score >= 1000:
        print('Zanzibar')

    elif 800 <= turn_score < 1000:
        print('Three of a kind!')

    elif 500 <= turn_score < 800:
        print('123')

    return turn_score


# second = roll_score(4, 4, 4)
print(len(range(p_amount)))

for i in range(p_amount):

    rolls = roll_dice()
    points = (roll_score(*rolls))

    scoring_test.append(points)

print(points)
print(scoring_test)

    # if points != min(scoring_test):
    #     print("yellow")
