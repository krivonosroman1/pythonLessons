import turtle
t = turtle.Pen()
turtle.bccolor("black")
colors = ["red", "yellow", "blue", "green"]
your_name = turtle.textinput("Введите свое имя", "Как тебя зовут")
for x in range(100):
    t.pencolor(colors[x%4]
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Arial", int((x + 4) / 4),"bold"))
    t.left(90)
