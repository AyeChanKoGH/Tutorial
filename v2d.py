import tkinter as tk
from numpy import array,cos,sin,radians
x=tk.Tk()
canv=tk.Canvas(x,bg='black',height=400,width=600)
canv.pack()
#x=300+x'
#y=200-y'
def get_pos(point):
    return (300+point[0],200-point[1])
p1,p2=(0,0),(100,100)
p1n,p2n=get_pos(p1),get_pos(p2)
x0,y0=p1n
x1,y1=p2n
def rotation(point,ang):
    x,y=point
    ang=radians(ang)
    xn=(x*cos(ang))-(y*sin(ang))
    yn=(x*sin(ang))+(y*cos(ang))
    return (xn,yn)

canv.create_line(x0,y0,x1,y1,fill='green')
p1,p2=rotation(p1,45),rotation(p2,45)
p1n,p2n=get_pos(p1),get_pos(p2)
x0,y0=p1n
x1,y1=p2n
canv.create_line(x0,y0,x1,y1,fill='white')
x.mainloop()