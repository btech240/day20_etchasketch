from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_foward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clockwise():
    tim.right(10)


def move_counterclockwise():
    tim.left(10)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="c", fun=clear_screen)


# KEEP AT BOTTOM OF CODE - exits the app on click
screen = Screen()
screen.exitonclick()
