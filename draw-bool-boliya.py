import turtle as t
import random as rd
win=t.getscreen()
l=t.Turtle()
win.bgcolor('black')
l.speed(0)
move=30
add=move
# colors=["blue","green","red","cyan","magenta","yellow"]
colors=["blue","green","red"]

for o in range(20):
    for i in range(2):
        rd.shuffle(colors)
        l.color(colors[0])
        l.forward(move)
        l.right(90)
    move+=add
l.hideturtle()    
t.mainloop()
