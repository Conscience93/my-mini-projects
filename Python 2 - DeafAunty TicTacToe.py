## Challenges: Deaf Aunty
# import time

# name = input("What's your name? ")

# while True:
#     talk = input("Say something. ")

#     if talk.isupper():
#         print("YOU ARE VERY RUDE")
#     elif talk.islower():
#         print("WHAT? SPEAK UP!")        
#     elif talk.istitle():
#         print("SHOW SOME RESPECT!")
#     elif talk == "I love you aunty, I have to go now":
#         print("ok goodbye")
#         time.sleep(1)
#         print(f"{name}, are you there?")
#         what1 = input("")
#         if what1 == "":
#             print(f"{name}, are you there?")
#             what2 = input("")
#             if what2 == "":
#                 break
#     elif talk == "I SAY SOMETHING ITS RUDE. I TALK LOUDLY, ITS RUDE. I TALK SOFTLY, ITS RUDE. THEN WHAT SHOULD I FKING SAY???!!?!?":
#         print("hi")
#     else:
#         pass


## Challenges: Tic tac toe
player_turn = 1
winner = ""
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
    ]
        
def print_board():
    print("")
    print(board[0])
    print(board[1])
    print(board[2])
    print("")

def judge_player(player):
    global winner
    for i in range(0,2):
        if board[i][0] == marker and board[i][1] == marker and board[i][2] == marker:
            winner = f"Winner is Player {player}!"
            print(winner)

        if board[0][i] == marker and board[1][i] == marker and board[2][i] == marker:
            winner = f"Winner is Player {player}!"
            print(winner)

    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        winner = f"Winner is Player {player}!"
        print(winner)

    if board[0][2] == marker and board[1][1] == marker and board[2][0] == marker:
        winner = f"Winner is Player {player}!"
        print(winner)


# def judge_player2():
#     global winner
#     for i in range(0,2):
#         if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
#             winner = "Winner is Player 2!"
#             print(winner)

#         if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
#             winner = "Winner is Player 2!"
#             print(winner)

#     if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
#         winner = "Winner is Player 2!"
#         print(winner)

print(f"Player {player_turn}")
print("==========")

while True:
    x_coordinate = int(input("Put in your X coordinate: "))
    y_coordinate = int(input("Put in your Y coordinate: "))
    marker = "X" if player_turn == 1 else "O"
    if x_coordinate > 2 or y_coordinate > 2:
        print("hey, it's outta the tic-tac-toe board! dont make my life harder :(")
    elif board[x_coordinate][y_coordinate] != "-":
        print("hey, it's already taken! PICK ANOTHER COORDINATE PLZZZZZ")
    else:
        if player_turn == 1:
            board[x_coordinate][y_coordinate] = marker
            judge_player(player_turn)
            player_turn = 2    # change to player 2
        else:
            board[x_coordinate][y_coordinate] = marker
            judge_player(player_turn)
            player_turn = 1    # change to player 1

        print_board()
        if winner != "": break
        print(f"Player {player_turn}")
        print("==========")
