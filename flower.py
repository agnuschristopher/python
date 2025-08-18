import turtle
t = turtle.Turtle()
t.speed(10) 
def petal(radius):
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)
num_petals = int(input("Enter the number of petals: "))
size = int(input("Enter the size of petals (e.g., 50, 100): "))
for _ in range(num_petals):
    petal(size)
    t.right(360 / num_petals)
t.penup()
t.goto(0, -size // 4)
t.pendown()
t.begin_fill()
t.end_fill()
turtle.done()
