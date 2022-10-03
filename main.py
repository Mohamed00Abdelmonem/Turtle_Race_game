# This is a program turtle race
import random

from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the rice? Enter a color: ')

colors = ["red","yellow", "green", "blue"]
y_postions = [-70, -40, -10, 20, 50, 80, 110, 140]
all_turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-250 + 10, y=-y_postions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you'v won! the {winner_color} turtle in the winner!")
            else:
                print(f"you'v lose! the {winner_color} turtle in the winner!")

        rand_distance = random.randint(2, 12)

        turtle.forward(rand_distance)

screen.exitonclick()
