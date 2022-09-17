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

def output_pieces(spisok: list) -> None:
    count = 1
    for i in range(len(spisok)):
        print(str(count)+":"+str(spisok[i]))
        count += 1


def choice_element(spisok: list, flag: bool) -> list:
    """This is function"""
    pass

def print_game(spisok: list) -> None:
    print()
    for i in range(len(spisok)):
        print(spisok[i], end='')
    print()
    print()


domino = init_domino()
i = check_have_snacke()
j = check_have_snacke()
user_answer = 0
temp = []
temp.append(get_snake(max_element(i), max_element(j)))
while len(i) >= 0 and len(j) >= 0:
    print("=" * 70)
    print("Stock pieces: ", len(domino))
    print("Comouter pieces: ", len(i))
    print_game(temp)
    print("Your pieces: ")
    output_pieces(j)
    if len(i) > len(j):
        status = "Computer is about to make a move. Press Enter to continue..."
    else:
        status = "Status: It's your turn to make a move. Enter your command."
    print("Status: ", status )
    while True:
    user_answer = input()
    if user_answer > len(j) of < -len(j):
        print()
    if user_answer != '':
        if len(j):
            if int(user_answer) > 0:
                temp.append(j.pop(int(user_answer) - 1))
            else:
                temp.insert(0,j.pop(abs(int(user_answer)) - 1))
    else:
        if len(i):
            temp.append(i.pop(random.randint(0,len(i) - 1)))
else:
    if len(i):
        print("The game is over. You won!")
    elif len(j):
        print("The game is over. The computer won!")
    else:
        print("Status: The game is over. It's a draw!")






