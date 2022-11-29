from turtle import *
import random


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
        pass  # goto standard game
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


def player_text(player_id_number):
    penup()
    setposition(0, -210)

    color('black', 'green')
    pendown()
    write(f"Player {player_id_number}", move=False, align="center",
          font=("Cooper Black", 50, "normal"))

    penup()


def player_text_replace(player_id_number):
    penup()
    setposition(0, -210)

    color('green')
    pendown()
    write(f"Player {player_id_number}", move=False, align="center",
          font=("Cooper Black", 50, "normal"))

    penup()


def turn_text(number_of_turns):
    penup()
    setposition(0, -300)

    color('black', 'green')
    pendown()
    write(f"Turn {number_of_turns}", move=False, align="center",
          font=("Cooper Black", 50, "normal"))


def turn_deleter(number_of_turns):
    penup()
    setposition(0, -300)

    color('green')
    pendown()
    write(f"Turn {number_of_turns}", move=False, align="center",
          font=("Cooper Black", 50, "normal"))


def winner_text(player_number):


    penup()
    setposition(0, -210)

    color('black', 'gold')
    pendown()
    write(f"Congratulations Player {player_number + 1}", move=False, align="center",
          font=("Cooper Black", 50, "normal"))
    penup()
    setposition(0, -300)

    color('black', 'gold')
    pendown()
    write(f"You Win!", move=False, align="center",
          font=("Cooper Black", 50, "normal"))


def die_d0():
    # ####### Bottom Right Dice ######
    penup()
    setposition(100, -100)
    begin_fill()
    color('black', 'white')
    for _ in range(2):
        forward(200)
        left(90)
        forward(200)
        left(90)
    end_fill()


def die_d1():
    # ####### Bottom left dice #####
    t1.penup()
    t1.setposition(-300, -100)
    t1.begin_fill()
    t1.color('black', 'white')
    for _ in range(2):
        t1.forward(200)
        t1.left(90)
        t1.forward(200)
        t1.left(90)
    t1.end_fill()


def die_d2():

    # ###### Top Center dice ######
    t2.penup()
    t2.setposition(-100, 150)
    t2.begin_fill()
    t2.color('black', 'white')
    for _ in range(2):
        t2.forward(200)
        t2.left(90)
        t2.forward(200)
        t2.left(90)
    t2.end_fill()


# #### Top center dice sides #####
def d2_one():
    t2.penup()
    t2.setposition(0, 220)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()


def d2_two():
    t2.penup()
    t2.setposition(47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()


def d2_three():
    t2.penup()
    t2.setposition(0, 220)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()


def d2_four():
    t2.penup()
    t2.setposition(47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()


def d2_five():
    t2.penup()
    t2.setposition(0, 220)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(25)
    t2.end_fill()


def d2_six():
    t2.penup()
    t2.setposition(47, 220)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(20)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 220)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(20)
    t2.end_fill()

    t2.penup()
    t2.setposition(47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(20)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(20)
    t2.end_fill()

    t2.penup()
    t2.setposition(47, 170)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(20)
    t2.end_fill()

    t2.penup()
    t2.setposition(-47, 270)
    t2.begin_fill()
    t2.color('black', 'black')
    t2.pendown()
    t2.circle(20)
    t2.end_fill()


# #### Bottom left dice sides #####
def d1_one():
    t1.penup()
    t1.setposition(-198, -25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()


def d1_two():
    t1.penup()
    t1.setposition(-245, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()


def d1_three():
    t1.penup()
    t1.setposition(-198, -25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-245, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()


def d1_four():
    t1.penup()
    t1.setposition(-245, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-245, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()


def d1_five():
    t1.penup()
    t1.setposition(-198, -25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-245, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-245, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(25)
    t1.end_fill()


def d1_six():
    t1.penup()
    t1.setposition(-245, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(20)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(20)
    t1.end_fill()

    t1.penup()
    t1.setposition(-245, 25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(20)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, -75)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(20)
    t1.end_fill()

    t1.penup()
    t1.setposition(-245, -25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(20)
    t1.end_fill()

    t1.penup()
    t1.setposition(-150, -25)
    t1.begin_fill()
    t1.color('black', 'black')
    t1.pendown()
    t1.circle(20)
    t1.end_fill()


# ###### Bottom right dice sides #####
def d0_five():
    penup()
    setposition(150, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(150, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(250, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(250, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(200, -25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()


def d0_one():
    penup()
    setposition(200, -25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()


def d0_two():
    penup()
    setposition(150, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(250, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()


def d0_six():
    penup()
    setposition(150, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(20)
    end_fill()

    penup()
    setposition(150, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(20)
    end_fill()

    penup()
    setposition(150, -25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(20)
    end_fill()

    penup()
    setposition(250, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(20)
    end_fill()

    penup()
    setposition(250, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(20)
    end_fill()

    penup()
    setposition(250, -25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(20)
    end_fill()


def d0_three():
    penup()
    setposition(150, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(250, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(200, -25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()


def d0_four():
    penup()
    setposition(150, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(150, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(250, -75)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()

    penup()
    setposition(250, 25)
    begin_fill()
    color('black', 'black')
    pendown()
    circle(25)
    end_fill()


def player_names(x):
    p_names = []
    for i in range(x):
        p_name = input(f"Please enter player {i + 1} name: ")
        p_names.append(p_name)

    print('Players are:\n', end=' * ')
    [print(i, end=' * ') for i in p_names]
    print()

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
    :param roll1: First die roll
    :param roll2: Second die roll
    :param roll3: Third die roll
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
    #
    # if turn_score >= 1000:
    #     print('Zanzibar')
    #
    # elif 800 <= turn_score < 1000:
    #     print('Three of a kind!')
    #
    # elif 500 <= turn_score < 800:
    #     print('123')

    return turn_score


player_score = []

p_amount = int(input("How many people will be playing? "))

# player_names(p_amount)

# sets score for each player
for i in range(p_amount):
    player_score.append(5)
print(player_score)

# second = roll_score(4, 4, 4)
getscreen().bgcolor('green')

t1 = Turtle()
t2 = Turtle()

speed(0)
t1.speed(0)
t2.speed(0)

hideturtle()
t1.hideturtle()
t2.hideturtle()

scoring_test = []
turn_counter = 0


while min(player_score) > 0:
    turn_counter += 1
    turn_text(turn_counter)

# for loop is one turn
    for i in range(p_amount):

        rolls = roll_dice()

        roll1 = rolls[0]
        roll2 = rolls[1]
        roll3 = rolls[2]

        points = (roll_score(*rolls))

        scoring_test.append(points)

        player_text(i + 1)

        die_d1()
        if roll1 == 1:
            d1_one()
        elif roll1 == 2:
            d1_two()
        elif roll1 == 3:
            d1_three()
        elif roll1 == 4:
            d1_four()
        elif roll1 == 5:
            d1_five()
        elif roll1 == 6:
            d1_six()

        die_d2()
        if roll2 == 1:
            d2_one()
        elif roll2 == 2:
            d2_two()
        elif roll2 == 3:
            d2_three()
        elif roll2 == 4:
            d2_four()
        elif roll2 == 5:
            d2_five()
        elif roll2 == 6:
            d2_six()

        die_d0()
        if roll3 == 1:
            d0_one()
        elif roll3 == 2:
            d0_two()
        elif roll3 == 3:
            d0_three()
        elif roll3 == 4:
            d0_four()
        elif roll3 == 5:
            d0_five()
        elif roll3 == 6:
            d0_six()

        if i != p_amount:
            player_text_replace(i + 1)



        print(points)

    turn_deleter(turn_counter)

    print(scoring_test)

    # if points != min(scoring_test):
    #     print("yellow")

    loser = min(scoring_test)
    winner = max(scoring_test)

    if winner == 1000:
        loser_position = scoring_test.index(loser)
        player_score[loser_position] += (4 * (p_amount - 1))
        for player in range(len(player_score)):
            if player != loser_position:
                player_score[player] -= 4
            elif player == loser_position:
                pass

    elif winner == 800:
        loser_position = scoring_test.index(loser)
        player_score[loser_position] += (3 * (p_amount - 1))
        for player in range(len(player_score)):
            if player != loser_position:
                player_score[player] -= 3
            elif player == loser_position:
                pass

    elif winner == 500:
        loser_position = scoring_test.index(loser)
        player_score[loser_position] += (2 * (p_amount - 1))
        for player in range(len(player_score)):
            if player != loser_position:
                player_score[player] -= 2
            elif player == loser_position:
                pass

    else:
        loser_position = scoring_test.index(loser)
        player_score[loser_position] += (p_amount - 1)
        for player in range(len(player_score)):
            if player != loser_position:
                player_score[player] -= 1
            elif player == loser_position:
                pass

    print(f'Round Loser: {loser}')
    print(f'Round Winner: {winner}')
    print(f'Current Score: {player_score}')

    scoring_test = []

game_winner = min(player_score)

winner_position = player_score.index(game_winner)

winner_text(winner_position)

exitonclick()
