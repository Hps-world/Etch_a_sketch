from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race? Enter a color: ")
turtle_name=["sheer","gian","sheeru","noibita","himanshu"]

color=["red","green","blue","orange","yellow","purple"]
y=[100,50,0,-50,-100]
for turtle_index in range(5):
    turtle_name[turtle_index]=Turtle(shape="turtle")
    turtle_name[turtle_index].color(color[turtle_index])
    turtle_name[turtle_index].penup()
    turtle_name[turtle_index].goto(x=-230,y=y[turtle_index])

if user_bet in color:
    is_race_start=True
while is_race_start:

    for i in range(5):
        if turtle_name[i].xcor()>230:
            winning_color=turtle_name[i].pencolor()
            if(winning_color==user_bet):
                print(f"You've won!.{winning_color} turtle is the winner!")
                is_race_start=False
            else:
                print(f"you lost {winning_color} turtle is the winner")
                is_race_start=False
                
        random_distance = random.randint(0, 12)
        turtle_name[i].forward(random_distance)



screen.exitonclick()