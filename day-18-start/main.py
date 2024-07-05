# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# from turtle import * -> 지양하는 import 방식이다. 메서드가 어디서 온건지 모르기 때문
# from random import * -> 를 예로 들었을 때 choice([1, 2, 3])의 경우 choice가 너무 보편적인 메서드기 때문에 random인걸 알아차리기
# 어려울 수가 있다.

# from turtle import Turtle, Screen
# tim = Turtle()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.pencolor("white")
#     tim.forward(10)
#     tim.pencolor("black")

import turtle as t

tim = t.Turtle()

# for n in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#

#
# import heroes
#
# print(heroes.gen())
#

import random
t.colormode(255)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.speed("fastest")
def random_color():
    colours = []
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         t.forward(100)
#         t.right(angle)
#
# for _ in range(3, 11):
#     t.color(random.choice(colours))
#     draw_shape(_)

directions = [ 0, 90, 180, 270 ]

# t.width(5)
# colours = random_color()
# for _ in range(200):
#     t.forward(30)
#     t.setheading(random.choice(directions))
#     t.color(random_color())

# for _ in range(200):
#     t.circle(100)
#     t.right(2)
#     t.color(random_color())

# 풀이버전

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        current_heading = t.heading()
        t.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()