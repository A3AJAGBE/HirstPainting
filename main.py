import turtle
import colorgram

sample = turtle.Turtle()
screen = turtle.Screen()
screen.title('Sample of Hirst Contemporary Spot Painting')

# Extract 10 colors from the hirst sample image.
hirst_color = []
colors = colorgram.extract('image.jpg', 15)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    hirst_color.append(rgb_color)

print(hirst_color)


screen.exitonclick()
