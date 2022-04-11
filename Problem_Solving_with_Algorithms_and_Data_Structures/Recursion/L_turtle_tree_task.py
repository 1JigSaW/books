import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        tt = random.randrange(15, 25)
        t.right(tt)
        tree(branchLen-random.randrange(1, 30),t)
        t.left(40)
        tree(branchLen-random.randrange(1, 30),t)
        t.right(tt)
        t.backward(branchLen)

t = turtle.Turtle()
myWin = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(75,t)
myWin.exitonclick()