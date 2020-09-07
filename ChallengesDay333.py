import re
import string
import random

## Savage Boggle Raid (ffxiv reference)

sample_board = [
    ["U","N","O","T"],
    ["S","E","W","G"],
    ["S","V","L","T"],
    ["L","Qu","C","F"]
]

def check(board, word):
    Found = False
    Found2 = False
    x = 0
    y = 0
    split_word = []
    split_word[:] = word
    checking_first_letter = split_word[0]
    checking_remaining_letter = split_word[1:]
    print(checking_remaining_letter)
    while Found != True:
        for y in range(0,4):
            for x in range(0,4):
                target_letter = sample_board[x][y]
                if target_letter == checking_first_letter:
                    Found = True
                    x2 = x
                    y2 = y 
                    print(str(x2) + " " + str(y2))
                    break
    
    while Found2 != True:
        for y in range(-1,2):
            if y < 0:
                pass
            else:
                for x in range(-1,2):
                    if x < 0:
                        pass
                    else:
                        target_letter = sample_board[x][y]
                        if target_letter == checking_remaining_letter[0]:
                            Found2 = True
                            x2 = x
                            y2 = y 
                            print(str(x2) + " " + str(y2))
                            break

check(sample_board, "SE")

