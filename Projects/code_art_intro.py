# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("green")
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(45)
    t.forward(90)


# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################