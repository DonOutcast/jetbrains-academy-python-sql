#!/usr/bin/env python3
import random


def init_domino() -> list:
    """This is function for domino range"""
    full_domino = []
    spisok = []
    for i in range(7):
        for j in range(7):
            spisok.append(i)    
            spisok.append(j)
            full_domino.append(spisok)
            spisok = []
    return full_domino


def pieces() -> list:
    """This is function retunr list of domino"""
    global domino
    pieces = []
    for i in range(8):
        for_delete_and_push = random.choice(domino)
        pieces.append(for_delete_and_push)
        domino.remove(for_delete_and_push)
    # print(domino)
    # print()
    # print()
    # print(pieces)
    return pieces

domino = init_domino()

i = pieces()
j = pieces()
max_i = []
max_j = []
big = []

def where_max(pieces_1, pieces_2) -> list:
    max_i = []
    max_j = []
    temp_i = pieces_1[0]
    temp_j = pieces_2[0]
    snake = []
    for i in pieces_1:
        if temp_i[0]  < i[0] and :
            temp_i = i;
    for l in pieces_1:
        if temp_i[1] < i[1] and temp_i[0]  >= i[0]:
            temp_i = i

    max_i.append(temp_i)
    # for j in pieces_2:
    #     if temp_j[0] < j[0] and temp_j[1] < j[1]:
            # temp_j = j
            # if temp_j[1] < j[1]:
                # temp_j = j
    # max_j.append(temp_j)
    print("I ",max_i)
    print("J" ,max_j)


for (k ,l) in zip(i, j):
    print(k, l)

print()
where_max(i, j)


# print(pieces(i), "\n")
# print(pieces(i), "\n")
# print(i, "\n")


