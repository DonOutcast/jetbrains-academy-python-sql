# Part 1
Theory
Note:
Before you start this project, it's better to get familiar with the basic domino rules. Keep in mind that there are many versions of the game. The rules used in this particular project will be described as we go along.

As you might know, a domino is a playing piece that is characterized by the two numbers written on it. The numbers are integers and can range from 0 to 6. A single domino piece has no orientation, so, a full domino set (that includes all the possible pairs of numbers) will have 28 unique dominoes.

You may think that there should be 7*7=49 dominoes in total. However, this is not the case because the combinations like [1,2] and [2,1] are the same domino, not two separate ones.

Description
To play domino, you need a full domino set and at least two players. In this project, the game is played by you and the computer.

At the beginning of the game, each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces).

To start the game, players determine the starting piece. The player with the highest domino or the highest double ([6,6] or [5,5] for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed.

Status is the player, who is to make the next move
Objectives
Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either "player" or "computer".
Stock pieces      # 14 domino elements
Computer pieces   # 7 or 6 domino elements
Player pieces     # 6 or 7 domino elements
Domino snake      # 1 starting domino
Status            # the player that goes first
If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
Output all five variables.
Examples
Example 1

The player makes the first move.

Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
Domino snake: [[6, 6]]
Status: player

Example 2

The computer makes the first move.

Stock pieces: [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3]]
Computer pieces: [[0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5]]
Player pieces: [[1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4]]
Domino snake: [[5, 5]]
Status: computer
# Part 2
Description
A good game needs a good interface. In this stage, you will make your output user-friendly.

The player should be able to see the domino snake, the so-called playing field, and their own pieces. It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.

Two things must remain hidden from the player: the stock pieces and the computer's pieces. The player should not be able to see them, only the number of pieces remaining.

Objectives
Print the header using seventy equal sign characters (=).
Print the number of dominoes remaining in the stock – Stock size: [number].
Print the number of dominoes the computer has – Computer pieces: [number].
Print the domino snake. At this stage, it consists of the only starting piece.
Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
Print the status of the game:
If status = "computer", print "Status: Computer is about to make a move. Press Enter to continue..."
If status = "player", print "Status: It's your turn to make a move. Enter your command."
Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.
Examples
Example 1

The player makes the first move (status = "player")

======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.

Example 2

The Computer makes the first move (status = "computer")

======================================================================
Stock size: 14
Computer pieces: 7

[5, 5]

Your pieces:
1:[1, 3]
2:[1, 4]
3:[4, 5]
4:[1, 6]
5:[1, 1]
6:[0, 4]

Status: Computer is about to make a move. Press Enter to continue...
