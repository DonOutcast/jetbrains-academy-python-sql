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
    for i in range(7):
        for_delete_and_push = random.choice(domino)
        pieces.append(for_delete_and_push)
        domino.remove(for_delete_and_push)
    return pieces


def check_have_snacke(spisok: list) -> list:
    flag = 0
    while flag != 1:
        spisok = pieces()
        for i in spisok:
            if i[0] == i[1]:
                flag = 1
    return spisok

def max_element(spisok_1) -> list:
    temp_i = []
    for i in spisok_1:
        if i[0] == i[1]:
            temp_i = i
    return temp_i
def get_snacke(spisok_1, spisok_2) -> list:
    global i, j
    if spisok_1[0] > spisok_2[0]:
        return i.pop(i.index(spisok_1))
    return j.pop(j.index(spisok_2))

domino = init_domino()
i = check_have_snacke(pieces())
j = check_have_snacke(pieces())
print(get_snacke(max_element(i), max_element(j)))
print("Stock pieces: ", domino)
print("Comouter pieces: ",i)
print("Player pieces: ",j)
if len(i) > len(j):
    status = "Computer"
else:
    status = "Player"
print("Status: ", status )
print(type(i[0]))
