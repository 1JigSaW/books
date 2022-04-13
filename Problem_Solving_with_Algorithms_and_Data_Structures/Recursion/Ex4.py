import turtle

def mountains(t, line):
    if line > 0:
        t.right(20)
        t.forward(line-15)
        t.left(130)
        mountains(t, line-5)
        t.forward(line-15)
        t.right(20)
        t.forward(line-15)
        mountains(t, line-5)

t = turtle.Turtle()
myWin = turtle.Screen()
t.left(90)
mountains(t, 100)
myWin.exitonclick()