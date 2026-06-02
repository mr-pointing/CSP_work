#   a123_apple_1.py
import turtle as trtl

# setup
apple_image = "pear.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()

drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.goto(-10, -30)


# functions
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()


def apple_fall():
    drawer.clear()
    apple.penup()
    apple.goto(0, -150)


def turtle_clicked(x, y):
    apple_fall()


# function calls
draw_apple(apple)
drawer.color("blue")
drawer.write("A", font=("Arial", 30, "bold"))

# wn.onkeypress(draw_an_A, "a")
wn.onkeypress(apple_fall, "a")
wn.listen()
wn.mainloop()
