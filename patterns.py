import turtle as t
win=t.getscreen()
pat=t.Turtle()
t.hideturtle()
win.bgcolor('black')
pat.color('white')
win.listen()
# draw circle pattern with events binds
class patterns:
    def __init__(self,distance,ang) -> None:
        self.dis=distance
        self.ang=ang
        self.keys()
        self.s=False
    def keys(self):
       win.onkeypress(lambda:pat.forward(self.dis),'Up')
       win.onkeypress(lambda:pat.backward(self.dis),'Down')
       win.onkeypress(lambda:pat.right(self.ang),'Right')
       win.onkeypress(lambda:pat.left(self.ang),'Left')
       win.onkeypress(self.sqaure,'s')
       win.onkeypress(lambda:pat.clear(),'r')

    def swich(self):
        self.s=True
    def sqaure(self,dis=100,angle=10,tm=100):
        for t in range(tm):
            for l in range(4):
                pat.forward(dis)
                pat.left(90)
                win.onkeypress(self.swich,'q')
                if self.s:
                    break
            pat.right(angle)
            if self.s:
                break


# pat1=patterns(distance=50,ang=45)  

t.mainloop()

