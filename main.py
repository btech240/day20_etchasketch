from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_foward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_foward)


# KEEP AT BOTTOM OF CODE - exits the app on click
screen = Screen()
screen.exitonclick()
