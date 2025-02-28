# Etch-A-Sketch App

from turtle import Turtle,Screen
sheer=Turtle()
def move_forwards():
    sheer.forward(20)
def move_backwards():
    sheer.backward(20)
def turn_left():
    sheer.left(10)
def turn_right():
    sheer.right(10)
screen=Screen()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.exitonclick()




