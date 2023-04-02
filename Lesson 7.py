import turtle

turtle.begin_fill()

turtle.color('black', 'red')
turtle.bgcolor('blue')

for i in range(4):
    turtle.right(90)
    turtle.forward(100)

turtle.clear()

for i in range(25):
    turtle.right(15)
    turtle.forward(10)

turtle.clear()

for i in range(80):
    turtle.right(15)
    turtle.forward(10+i)

colors = ['red','orange','yellow','green','blue','purple']

turtle.circle(25)

num = 500

n_color = 0

for i in range(400):
    turtle.color(colors[n_color])
    turtle.right(15)
    turtle.forward(num - i)

