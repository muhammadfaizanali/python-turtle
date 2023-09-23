# import turtle as t
# win=t.getscreen()
# choto=t.Turtle()
# t.hideturtle()
# win.bgcolor('black')
# choto.color('blue')
# choto.speed(0)
# radius=10
# rd=radius
# for n in range(20):
#     for i in range(1,3):
#         if i%2==0:
#             choto.circle(radius*-1)
#         else:
#             choto.circle(radius)
#     radius+=rd        
# t.mainloop()


# 4 circle draw
import turtle as t
import random as rand
win=t.getscreen()
choto=t.Turtle()
t.hideturtle()
win.bgcolor('black')
choto.color('white')
choto.speed(0)
radius=5
rd=radius
colors=["blue","green","cyan","magenta"]   
def main(x,y):
    global radius
    radius=rd
    choto.penup()
    choto.goto(x,y)
    choto.pendown()
    for n in range(10):
        choto.right(90)
        for i in range(1,3):
            if i%2==0:
                rand.shuffle(colors)
                choto.color(colors[0])
                choto.circle(radius*-1)
            else:
                rand.shuffle(colors)
                choto.color(colors[0])
                choto.circle(radius)
        choto.left(90)        
        for i in range(1,3):
            if i%2==0:
                rand.shuffle(colors)
                choto.color(colors[0])
                choto.circle(radius*-1)
            else:
                rand.shuffle(colors)
                choto.color(colors[0])
                choto.circle(radius)   
        radius+=rd 
win.onclick(main)    

t.mainloop()



