import colorgram
import turtle as t
import random

t.colormode(255)
daimen = t.Turtle()

# colors = colorgram.extract("ColorPallet.jpeg", 40)

pallet = [(246, 244, 243), (235, 239, 246), (241, 246, 243), (247, 239, 242), (135, 164, 199), (223, 151, 105),
          (31, 44, 63), (200, 137, 148), (160, 61, 51), (235, 212, 93), (49, 100, 139), (138, 181, 162), (147, 64, 72),
          (56, 49, 47), (161, 32, 30), (62, 115, 100), (228, 165, 171), (51, 40, 43), (169, 29, 33), (210, 86, 76),
          (236, 167, 156), (34, 60, 54), (16, 95, 70), (34, 60, 105), (171, 188, 219), (191, 101, 109), (109, 127, 155),
          (174, 200, 191), (36, 149, 206), (20, 83, 104), (64, 66, 57), (157, 201, 221), (101, 141, 131),
          (131, 128, 121)]

# for color in colors:
#     pallet.append(tuple(color.rgb))
#
# print(pallet)
daimen.speed(10)


def draw_horizontally():
    for _ in range(20):
        daimen.dot(20, pallet[random.randint(0, 33)])
        daimen.penup()
        daimen.forward(50)


x = -270
y = -270

for _ in range(10):
    daimen.penup()
    daimen.setposition(x, y)
    draw_horizontally()
    y += 35

screen = t.Screen()
screen.exitonclick()
