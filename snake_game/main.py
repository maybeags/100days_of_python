from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600) # 키워드 인수 -> 나중에 코드 보는 사람이 편하다 (600, 600)보다
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# x_position = [0, -20, -40]

# all_turtles = []
# for i in range(0, 3):
#     new_turtle = Turtle("square")
#     new_turtle.color("white")
#     new_turtle.goto(x_position[i], 0)
#     all_turtles.append(new_turtle)

'''
강의 부분
'''

# segments = [
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



    # for seg_num in range(len(segments) -1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)








screen.exitonclick()
