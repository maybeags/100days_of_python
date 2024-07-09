
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def move_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def clear_screen():
#     tim.home()
#     tim.clear()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)        # 함수를 다른 함수에 전달할 때는 끝에 괄호를 추가하지 않음.
# screen.onkey(key="s", fun=move_backwards)        # 함수를 다른 함수에 전달할 때는 끝에 괄호를 추가하지 않음.
# screen.onkey(key="d", fun=move_right)        # 함수를 다른 함수에 전달할 때는 끝에 괄호를 추가하지 않음.
# screen.onkey(key="a", fun=move_left)        # 함수를 다른 함수에 전달할 때는 끝에 괄호를 추가하지 않음.
# screen.onkey(key="c", fun=clear_screen)        # 함수를 다른 함수에 전달할 때는 끝에 괄호를 추가하지 않음.
#

'''

고차함수 Higher Order Functions : 다른 함수와 함께 작동하는 함수

def function_a(something):
    #Do this with something
    #then do this
    #finally do this
    
def function_b():
    #Do this
    
function_a(function_b)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    
def calculator(n1, n2, func):
    return func(n1, n2)
    
result = calculator(2, 3, divide)
print(result)
'''


'''
이거는 gpt
'''
# turtles = []
# start_y = -100
# for i in range(len(turtle_names)):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[i])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=start_y + (i *40))
#     turtles.append(new_turtle)

'''
여기는 강의
거북이 크기 40 by 40 (pixels)
'''
from turtle import Turtle, Screen
import random

is_race_on = False
# tim = Turtle()
screen = Screen()


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will the race? Enter a color: ").lower()
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# turtle_names = ["tom", "john", "jane", "jaime", "timmy", "jimmy"]

y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()