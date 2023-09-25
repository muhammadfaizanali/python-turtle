import turtle as t
import random as rd
win=t.getscreen()
pat=t.Turtle()
t.hideturtle()
win.bgcolor('white')
pat.color('white')
colors=["blue","green","cyan","magenta",'orange','yellow','pink'] 

# def design1():
    # pat.speed(0)
    # t.tracer(100)
#     while True:
#         pat.penup()
#         pat.goto(0,0)
#         pat.pendown()
#         pat.hideturtle()
#         for i in range(20):
#             rd.shuffle(colors)
#             pat.color(colors[0])
#             pat.circle(5+i*5)
#             pat.left(90)
#             pat.penup()
#             pat.forward(10)
#             pat.pendown()
#             pat.right(90)
#         pat.left(45)    
# design1()
# def design2():
#     pat.hideturtle()
#     pat.speed(0)
#     t.tracer(500)
#     while True:
#         a=2
#         pat.penup()
#         pat.goto(0,0)
#         pat.pendown()
#         for i in range(50):
#             rd.shuffle(colors)
#             pat.color(colors[0])
#             pat.circle(100,360)
#             pat.left(a)
#             a+=2
# design2()
# def design3():
#     pat.speed(0)
#     t.tracer(100)
#     pat.hideturtle()
#     a=2
#     while True:
#         if a%2==0:
#             for i in range(50):
#                 rd.shuffle(colors)
#                 pat.color(colors[0])
#                 pat.circle(100, 360)
#                 pat.left(5)
#             a=1 
#         else:
#             colorlist=['red','green','blue','pink']
#             for i in range(50):
#                 rd.shuffle(colorlist)
#                 pat.color(colorlist[0])
#                 pat.circle(100, 360)
#                 pat.right(5)
#             a=2        
# design3()        
def design4():
    pat.speed(0)
    t.tracer(500)
    pat.hideturtle()
    pat.pensize(3)
    while True:
        pat.penup()
        pat.goto(0,0)
        pat.down()
        for i in range(300):
            pat.color('black')
            pat.forward(i)
            pat.left(50)
design4()
t.mainloop()        