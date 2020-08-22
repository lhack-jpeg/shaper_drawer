import turtle

wn = turtle.Screen()
john = turtle.Turtle()

sides = int(input("Please enter the number of sides to draw: "))
sides = abs(sides)
angles = 360/sides

for x in range(sides):
    john.forward(50)
    john.left(angles)

