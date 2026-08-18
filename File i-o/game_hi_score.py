'''
The game() function in a program lets a user play a game and returns the score as an integer.
You need to read a file "Hi-score.txt" which is either blank or contains the previous Hi-score.
You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
'''

import random
def game():
    score = random.randint(1,100)

    with open("Hi-score.txt", "r") as h:
        hiscore = h.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = int(0)
    print(f"Your Score: {score}")

    if(score > hiscore):

        with open("Hi-score.txt", "w") as t:
            t.write(str(score))

    # return score


game()