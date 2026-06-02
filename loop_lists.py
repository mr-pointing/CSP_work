# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)

#
startx = 0
starty = 0

# Richard Pointing Block 2 Submission 1
# Loop to give each turtle a unique color and move them
for t, c in zip(my_turtles, turtle_colors):
    t.color(c)
    t.goto(startx, starty)
    t.right(45)
    t.forward(50)
    startx += 50
    starty += 50

wn = trtl.Screen()
wn.mainloop()
