"""
East Coast Crew: Act. Wordle (1.2.5)
6/2/26
Recreating the game Wordle to be played via the Turtle library
"""

# Imports
import random as r
import turtle as t

# Turtle Env Variables
sc = t.Screen()
sc.setup(900, 1000)
sc.bgcolor("#121212")
row_start_x = -275
row_start_y = 300
letter_start_x = -240
letter_start_y = 230
boxer = t.Turtle()
boxer.color("#fcfffa")
boxer.speed(0)
boxer.hideturtle()


# Game Functions
def make_boxes(first_x, first_y):
    boxer.penup()
    boxer.goto(first_x, first_y)
    boxer.pendown()

    for x in range(5):
        for i in range(4):
            boxer.forward(90)
            boxer.right(90)
        first_x += 110
        boxer.penup()
        boxer.goto(first_x, first_y)
        boxer.pendown()


def word_checker(user_answer, target):
    return_list = []
    for i in range(len(target)):
        if user_answer[i] == target[i]:
            return_list.append(True)
        elif user_answer[i] in target:
            return_list.append("maybe")
        else:
            return_list.append(False)
    print(return_list)
    return return_list

def get_color(ans):
    if ans is True:
        return "green"
    elif ans is False:
        return "#fcfffa"
    else:
        return "orange"

def write_word(user_word, target, letter_x, letter_y):
    answer = word_checker(user_word, target)
    checks = []

    for i in range(5):
        print(checks)
        boxer.penup()
        boxer.goto(letter_x, letter_y)
        boxer.pendown()
        boxer.color(get_color(answer[i]))
        boxer.write(user_choice[i], font=("Arial", 30, "bold"))
        letter_x += 110
        if answer[i] is True:
            checks.append("y")
        if len(checks) == 5:
            break
    return checks


# Game Variables
words = ["bytes", "mouse", "input", "logic", "array"]
word_choice = r.choice(words)

for i in range(5):
    make_boxes(row_start_x, row_start_y)
    row_start_y -= 100

for i in range(5):
    user_choice = t.textinput("Picka Word", "Insert word to be guessed").lower()
    ans_list = write_word(user_choice, word_choice, letter_start_x, letter_start_y)
    if len(ans_list) == 5:
        user_restart = t.textinput("Congratulations!",
                                   "Would you like to try again?\n(Yes for again, No for Quit.)").lower()
        if user_restart == "no":
            exit()
        else:
            pass
    letter_start_y -= 100


sc.mainloop()
