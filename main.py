from turtle import Turtle, Screen
import random

screen = Screen()


"""
##### Practicing Examples #####

# tim = Turtle()
# def move_forward():
#     tim.forward(50)
#
# def move_backward():
#     tim.backward(50)
#
# def move_counter_clockwise():
#     tim.left(10)
#     print(tim.heading())
#
# def move_clockwise():
#     tim.right(10)
#
# def clear():
#     tim.reset()
#
# def up():
#     tim.circle(radius=80, extent=10)
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear)
# screen.onkey(key="Up", fun=up)

"""
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x_coord = -230
y_coord = -100
is_on_true = False

turtles_list = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=x_coord, y=y_coord)
    y_coord = new_turtle.ycor() + 40
    new_turtle.color(color)
    turtles_list.append(new_turtle)


if user_bet:
    is_on_true = True

while is_on_true:
    for turtle in turtles_list:
        if turtle.xcor() >= 230:
            is_on_true = False
            if turtle.pencolor() == user_bet:
                print(f"You've win! The {turtle.pencolor()} turtle wins. ")
            else:
                print(f"You've Lose! The {turtle.pencolor()} turtle  wins. ")

        distance = random.randint(0, 10)
        turtle.forward(distance)



screen.exitonclick()