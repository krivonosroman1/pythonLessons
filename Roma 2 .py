import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(1):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
