# lists = ["Apple", "banana"]
# enumd1 = tuple(enumerate("lists"))
# enumd = tuple(enumerate(lists))
# enumd3 = dict(enumerate(lists))
# print(enumd)
# print(enumd1)
# print(enumd3)
# ################################phon number
# phon_number = {1: "One",
#                2: "Two",
#                3: "Ttree",
#                4: "Four"}
# phon_number_digit = str(input())
# print(phon_number_digit)
# for i in phon_number_digit:
#     print(phon_number[int(i)], end=" ")
#########################################
# def message_input(message: str):
#     words = message.split(' ')
#     emojis = {
#         ":)": '😊',
#         ":(": '🙁'
#     }
#     outp = ''
#     for word in words:
#         outp += emojis.get(word, word) + " "
#     return (outp)
# p = message_input("Hii am angry today :)")
# print(p)
import random

###########################################
#import numpy
#from random import Random
import random
#import matplotlib.pyplot as plt
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j] = random.randrange(0, 3)
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end="\t")
    print()
def board_set_zero(name_of_board):
    l = []
    for i in range(len(name_of_board)):
        for j in range(len(name_of_board[i])):
            #name_of_board[i][j] = random.randrange(0, 3)
            if name_of_board[i][j] == 0:
                l.append((i, j))
    #print(l)
    if l != []:
        g = l[random.randrange(len(l))]
    else:
        g = []
    return g
def board_win(name_of_board):
    s = 0
    k = 0
    n = 0
    m = 0
    d = False
    a = False
    for i in range(len(name_of_board)):
        if name_of_board[i].count(1) == len(name_of_board) or name_of_board[i].count(2) == len(name_of_board):
            #print("Win")
            d = True
        else:
            pass
        v = 0
        b = 0
        for j in range(len(name_of_board[i])):
            if name_of_board[i][j] == 1 and i == j:
                n += 1
            elif name_of_board[i][j] == 2 and i == j:
                m += 1
            if name_of_board[len(name_of_board[i]) - i - 1][j] == 1 and i == j:
                s += 1
            elif name_of_board[len(name_of_board[i]) - i - 1][j] == 2 and i == j:
                k += 1
            if name_of_board[j][i] == 1:
                v += 1
            elif name_of_board[j][i] == 2:
                b += 1

        if s == 3 or k == 3 or v == 3 or b == 3 or n == 3 or m == 3:
            a = True
        else:
            pass
    return (a or d)



print(board_set_zero(board))
print(board_win(board))



# print(len(board))
# print(board)
# for i in
# if board[i][j] == 0:
#     board[i][j]