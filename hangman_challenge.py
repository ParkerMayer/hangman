# Basic hangman game
# 11.10.20
# Author: Ochoa con ayuda de "Self Taught Programmer"

import random

# Hangman function
def hangman(word):
    wrong = 0
    stages = ["",
                "_________",
                "|                ",
                "|        |       ",
                "|        0       ",
                "|       /|\      ",
                "|       / \      ",
                "|                ",
             ]
    rletters = list(word)
    board = ["___"] * len(word)
    win = False
    print("\nWelcome to Hangman!")

    while wrong < len(stages) - 1:
        print ("\n")
        msg = "Guess a letter: "
        char = input(msg)
        
        if char in rletters:
            char_index = rletters.index(char)
            board[char_index] = char
            rletters[char_index] = "$"

        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "___" not in board:
            print("You win!")
            print("The word was: " + " ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong+1]))
        print("You lose! The word was {}.".format(word))


list_o_words = ["volvo", "library", "woman", "man", "person", "camera", "tv"]

x = random.randint(0, len(list_o_words) - 1)

hangman(list_o_words[x])
