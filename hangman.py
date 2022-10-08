def hangman(word):
    wrong = 0
    stages = ["",
              "________           ",
              "|                  ",
              "|         |        ",
              "|         0        ",
              "|        /|\       ",
              "|        / \       ",
              "|                  ",
              ]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome on execution!")

    while wrong < len(stages)-1:
        print("\n")
        msg = "Input a letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("YOU WON!!! THE WORD WAS: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print ("YOU LOST!!! THE WORD WAS: {}.".format(word))
import random
w = random.randint(0,7)
words= ["PAVEL",
        "KRISTINA",
        "ANNA",
        "MICHAEL",
        "EVGENIY",
        "LIDIYA",
        "VALERIY"]
t = words[w]
hangman(t)
               
