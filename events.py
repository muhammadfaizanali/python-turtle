import turtle as t
win=t.getscreen()
win.bgcolor("black")
t.hideturtle()
jack=t.Turtle()
jack.color('white')
def reset(x,y):
    jack.reset()
def sqaure(x,y):
    jack.pensize(5)
    jack.speed(0)    
    jack.color('blue')
    jack.penup()
    jack.goto(x,y)
    jack.showturtle()
    jack.pendown()
    jack.speed('slow')
    for l in range(4):
        jack.forward(100)
        jack.left(90)
    jack.hideturtle()

win.onclick(sqaure)      
win.onclick(reset,btn=3)      



t.mainloop()