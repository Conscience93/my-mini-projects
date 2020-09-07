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

x = 0
y = 0

def check(board, word):
    Found = False
    Found2 = False
    split_word = []
    split_word[:] = word
    checking_first_letter = split_word[0]
    checking_remaining_letter = split_word[1:]
    print(checking_remaining_letter)
    global x
    global y
    x2 = 0
    y2 = 0
    while Found != True:
        for i in range(0,4):
            for j in range(0,4):
                target_letter = sample_board[j][i]
                if target_letter == checking_first_letter:
                    Found = True
                    x2 = i
                    y2 = j 
                    # print(str(x2) + " " + str(y2))
                    break

    for num in range(0, len(checking_remaining_letter)):
        while Found2 != True:
            for i in [-1,0,1]:
                print(str(x2) + " " + str(y2))
                y2 += i
                if y2 == -1:
                    pass
                else:
                    for j in range(-1,2):
                        x2 += j
                        if x2 < 0:
                            pass
                        else:
                            target_letter = sample_board[x2][y2]
                            if target_letter == checking_remaining_letter[num]:
                                Found2 = True
                                print(str(x2) + " " + str(y2))
                                break
            if Found2 != True:
                print("oh no")
                break

check(sample_board, "SEW")

