import turtle as t
import random as r
robot = t.Turtle()
win=t.getscreen()
win.bgcolor("black")
robot.color("Blue")
robot.speed(0)
colors=["blue","green","red","cyan","magenta","yellow"]
mainDistence=5
distence=mainDistence
circlTime=100
for i in range(circlTime):
    robot.down()
    r.shuffle(colors)
    robot.color(colors[0])
    robot.circle(distence)
    robot.penup() 
    robot.right(90)
    robot.forward(mainDistence)
    robot.left(90)
    distence+=mainDistence
t.mainloop()