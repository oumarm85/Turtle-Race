import random
from turtle import Turtle, Screen

screen = Screen()
screen.bgpic("turtle_track.png")
screen.setup(width=848, height=1261)
race_started = False

user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
y_position = [-550, -330, -110, 110, 330, 550]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-385, y=y_position[index])
    new_turtle.speed(10)
    all_turtles.append(new_turtle)

race_started = True

while race_started:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            winner = turtle.pencolor()
            race_started = False
            if winner == user_bet:
                print(f"You Won! The {winner} turtle was first to cross the finish line!")
            else:
                print(f"You Lost! The {winner} turtle was first to cross the finish line!")
        else:
            movement = random.randint(0, 10)
            turtle.forward(movement)


screen.exitonclick()