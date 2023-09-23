import turtle as t
import random as r
robot = t.Turtle()
win=t.getscreen()
win.bgcolor("black")
robot.color("Blue")
robot.speed(0)
distence=1
squareTime=25
colors=["blue","green","red","cyan","magenta","yellow"]
for i in range(squareTime*4):
    r.shuffle(colors)
    robot.color(colors[0])
    robot.forward(distence)
    robot.left(90)
    distence+=10
t.mainloop()