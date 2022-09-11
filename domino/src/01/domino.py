import random


def init_domino() -> list:
    """This is function for domino range"""
    domino_set = []
    for i in range(0, 7):
        for j in range(i, 7):
            domino_set.append([i, j])
    return domino_set


def pieces(shrink) -> list:
    """This is function retunr list of domino"""
    global domino
    pieces = []
    for i in range(7):
        for_delete_and_push = random.choice(domino)
        pieces.append(for_delete_and_push)
        if shrink:
            domino.remove(for_delete_and_push)
    return pieces


def check_have_snacke() -> list:
    flag = 0
    shrink = True
    while flag != 1:
        spisok = pieces(shrink)
        for i in spisok:
            if i[0] == i[1]:
                flag = 1
        shrink = False
    return spisok


def max_element(spisok_1) -> list:
    temp_i = []
    temp = [0,0]
    for j in spisok_1:
        if j[0] == j[1] and j[0] > temp[0]:
            temp = j
    for i in spisok_1:
        if i[0] == i[1]:
            temp_i = i
    return temp

    
def get_snake(spisok_1, spisok_2) -> list:
    global i, j
    if spisok_1[0] > spisok_2[0]:
        return i.pop(i.index(spisok_1))
    return j.pop(j.index(spisok_2))

domino = init_domino()
i = check_have_snacke()
j = check_have_snacke()
temp = []
temp.append(get_snake(max_element(i), max_element(j)))
print("Stock pieces: ", domino)
print("Comouter pieces: ",i)
print("Player pieces: ",j)
if len(i) > len(j):
    status = "Computer"
else:
    status = "Player"
print("Domino snake: ", temp)
print("Status: ", status )

