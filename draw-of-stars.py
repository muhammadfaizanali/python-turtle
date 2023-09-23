import turtle as t
win=t.getscreen()
choto=t.Turtle()
def stars(x,y):
    for n in range(4):
        # choto.penup()
        for a in range(5):
            choto.left(144)
            choto.forward(100)
t.onclick(stars)            

t.mainloop()