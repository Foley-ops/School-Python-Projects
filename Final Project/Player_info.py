# def set_player():
#     p_list = []
#     p_score = []
#     p_amount = int(input("How many people will be playing? "))
#     for i in range(p_amount):
#         p_name = input(f"Please enter player {i + 1} name: ")
#         p_list.append(p_name)
#         p_score.append(20)
#
#     print('Players are: ', end=' * ')
#     [print(i, end=' * ') for i in p_list]
#
#     print(p_score)
#     return p_amount
#
#
# set_player()



def player_names(x):
    p_names = []
    for i in range(x):
        p_name = input(f"Please enter player {i + 1} name: ")
        p_names.append(p_name)

    print('Players are:\n', end=' * ')
    [print(i, end=' * ') for i in p_names]
    print()


def player_score(x):
    p_score = []
    for i in range(p_amount):
        p_score.append(20)
    print(f'Current Score\n{p_score}')



p_amount = int(input("How many people will be playing? "))
player_names(p_amount)
player_score(p_amount)