# Richard Pointing
# imports
import turtle as trtl
import random as r
import leaderboard as lb

# game configuration
lb_file_name = "leaderboard.csv"
player_name = input("Enter your name: ")
fill_color = "red"
size = 5
shape = "turtle"
score = 0

# timer variables
timer = 5
counter_interval = 1000  # 1000 represents 1 second
timer_up = False
counter = trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-380, -290)

# initialize moving turtle
raph = trtl.Turtle()
raph.shape(shape)
raph.turtlesize(size)
raph.color(fill_color)

# initialize score
score_turt = trtl.Turtle()
score_turt.penup()
score_turt.hideturtle()
score_turt.goto(380, -290)
font_setup = ("Arial", 60, "normal")


# game functions
# CODE TO ADD


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global score
    global raph

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(lb_file_name)
    leader_scores_list = lb.get_scores(lb_file_name)

    # show the leaderboard with or without the current player
    if len(leader_scores_list) < 5 or score >= leader_scores_list[4]:
        lb.update_leaderboard(lb_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, raph, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, raph, score)


def update_score():
    global score
    score += 1
    score_turt.clear()
    score_turt.write(score, font=font_setup)


def turtle_clicked(x, y):
    global timer_up
    if not timer_up:
        change_position()
        update_score()
    else:
        raph.hideturtle()


def change_position():
    x, y = r.randint(-400, 400), r.randint(-300, 300)
    raph.penup()
    raph.hideturtle()
    raph.goto(x, y)
    raph.showturtle()


def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


# events
raph.onclick(turtle_clicked)
window = trtl.Screen()
window.ontimer(countdown, counter_interval)
window.mainloop()
