"""
[summary]: run pip install PythonTurtle
 to install tutle.

"""
import turtle

# step2: set screen
pointer = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
colors = ['white','red','orange','yellow','green','blue']

# set initial pointer speed
pointer.speed(0)


for a in range(200):
    pointer.forward(a*4) # move pointer with some amount.
    pointer.right(91)  # shift right to make effect
    pointer.color(colors[a%6])  # change pointer color for next iteration
