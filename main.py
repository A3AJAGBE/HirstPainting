import random
import turtle
# import colorgram

sample = turtle.Turtle()
screen = turtle.Screen()
screen.title('Sample of Hirst Contemporary Spot Painting')

"""# Extract 10 colors from the hirst sample image.
hirst_color = []
colors = colorgram.extract('image.jpg', 15)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    hirst_color.append(rgb_color)

print(hirst_color)"""
colors = [(237, 229, 216), (237, 148, 70), (216, 231, 241), (243, 226, 236), (227, 242, 235), (28, 112, 164),
          (104, 175, 211), (168, 9, 38), (187, 172, 13), (163, 51, 95), (237, 82, 42), (10, 172, 212), (25, 132, 70),
          (188, 75, 32), (61, 15, 31)]
turtle.colormode(255)

sample.penup()
sample.goto(-290, -290)
sample.hideturtle()
sample.speed('fastest')

for dots in range(1, 131):
    sample.dot(30, random.choice(colors))
    sample.forward(50)

    if dots % 10 == 0:
        sample.setheading(90)
        sample.forward(50)
        sample.setheading(180)
        sample.forward(500)
        sample.setheading(0)


screen.exitonclick()
