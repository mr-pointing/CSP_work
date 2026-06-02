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
row_start_x = -275
row_start_y = 300
boxer = t.Turtle()
boxer.color("black")
boxer.speed(0)
boxer.hideturtle()


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


# Game Functions


# Game Variables
words = ["bytes", "mouse", "input", "logic", "array"]
target = r.choice(words)


user_choice = t.textinput("Picka Word", "Insert word to be guessed")

def word_checker(user_answer):
    while user_answer != target:
        for i in range(len(target)):
            if user_answer[i] == target[i]:
                print(f"{user_answer[i]} is correct and in the right spot")
            elif user_answer[i] in target:
                print(f"{user_answer[i]} is inside target and but in the wrong spot")
            else:
                print(f"{user_answer[i]} is not correct and not in the word")
        user_answer = input("Guess your word: ")

    print(f"Congrats on guessing {target}!")


for i in range(5):
    make_boxes(row_start_x, row_start_y)
    row_start_y -= 100

sc.mainloop()
