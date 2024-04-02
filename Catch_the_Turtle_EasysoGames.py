import turtle
import time
import math
from random import randint

font= ('Arial', 16, 'normal')

My_screen = turtle.Screen()
My_screen.bgcolor("light blue")
My_screen.title("Easyso Turtle Catch GAME")

turtle_instance = turtle.Turtle()

turtle_instance2 = turtle.Turtle()
turtle_instance2.penup()
turtle_instance2.hideturtle()

turtle_instance3 = turtle.Turtle()
turtle_instance3.penup()
turtle_instance3.hideturtle()

score=0
turtle_instance = turtle.Turtle('turtle')
speed = 1

num = math.floor(My_screen.numinput("Timer", "Enter the seconds", minval=0, maxval=59))
stop = False

turtle_instance.penup()
turtle_instance.setposition(randint(-300,300),randint(-300,300))

def change_position():
    turtle_instance.hideturtle()
    x = randint(-300,300)
    y = randint(-300,300)
    turtle_instance.penup()
    turtle_instance.goto(x,y)
    turtle_instance.pendown()
    turtle_instance.showturtle()

def update_score():
    global score
    score = score + 1
    turtle_instance3.clear()
    turtle_instance3.write(score, font=("Arial", 15))

def spot_clicked(x,y):

    global num
    if num > 0:
        update_score()
        change_position()
    else:
        turtle_instance.hideturtle()

My_screen.listen()
My_screen.onclick(spot_clicked, 1)

while True:
    turtle_instance2.sety(300)
    turtle_instance2.setx(-30)
    turtle_instance2.write(str(num), font=("Arial", 50))
    turtle_instance2.sety(370)
    turtle_instance2.setx(-50)
    turtle_instance2.write("Time Left:", font=("Arial", 15))
    num -= 1
    time.sleep(1)
    turtle_instance2.clear()

    if num <= 0:
        turtle_instance2.clear()
        turtle_instance2.sety(320)
        turtle_instance2.setx(-90)
        turtle_instance2.write("Time Over", font=("Arial", 30))
        time.sleep(5)
        turtle_instance2.clear()
        break
    print(num)
    My_screen.update()

turtle.mainloop()