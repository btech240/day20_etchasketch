import random
from turtle import Screen, Turtle

screen = Screen()

# Etch a sketch
# def move_foward():
#     tim.forward(10)


# def move_backward():
#     tim.backward(10)


# def move_clockwise():
#     tim.right(10)


# def move_counterclockwise():
#     tim.left()


# def clear_screen():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.home()


# screen.listen()
# screen.onkey(key="w", fun=move_foward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="a", fun=move_counterclockwise)
# screen.onkey(key="c", fun=clear_screen)
################################################################

#### Turtle Race ####

is_race_on = False

screen.setup(width=500, height=400)
colors = ["red", "orange", "green", "pink", "blue", "purple"]
all_turtles = []

# racers = [t1, t2, t3, t4, t5, t6]

user_winner = screen.textinput(
    title="Winner", prompt="Which turtle will win the race? Enter a color:")

if user_winner:
    is_race_on = True

yvalue = 100
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-240, y=-yvalue)
    all_turtles.append(new_turtle)
    yvalue -= 40


while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            is_race_on = False


if winning_color == user_winner:
    print(f"You won! {winning_color} won the race.")
else:
    print(f"{winning_color} won the race. You did not win.")


# KEEP AT BOTTOM OF CODE - exits the app on click
screen = Screen()
screen.exitonclick()
