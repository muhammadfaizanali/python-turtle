import turtle as t
win=t.getscreen()
win.bgcolor("black")
t.hideturtle()
jack=t.Turtle()
jack.color('blue')
def draggine(x,y):
    jack.ondrag(None)
    jack.setheading(jack.towards(x,y))
    jack.goto(x,y)
    jack.ondrag(draggine)
def move(x,y):
    jack.speed(0)
    jack.setheading(jack.towards(x,y))
    jack.penup()
    jack.goto(x,y)
    jack.pendown()
    jack.speed('slow')
def reset(x,y):
    jack.clear()
def main():
    win.listen()    
    jack.ondrag(draggine,btn=1)
    win.onclick(move,btn=1)            
    win.onclick(reset,btn=3)            
main()
t.mainloop()