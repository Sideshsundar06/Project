import tkinter as a
from tkinter import *
b=a.Tk()
b.title('calculator')
t= Entry(b)
t.grid(columnspan=4)
d= a.Button(b,activebackground="light blue" , bg="blue" ,text="1", width=5)
d.grid(row=2,column=1)
e= a.Button(b,activebackground="light green" , bg="green" ,text="2", width=5)
e.grid(row=2,column=2)
f= a.Button(b,activebackground="orange" , bg="red" ,text="3", width=5)
f.grid(row=2,column=3)
g= a.Button(b,activebackground="aqua" , bg="teal" ,text="4", width=5)
g.grid(row=3,column=1)
h= a.Button(b,activebackground="violet" , bg="indigo" ,text="5", width=5)
h.grid(row=3,column=2)
i= a.Button(b,activebackground="blue" , bg="light blue" ,text="6", width=5)
i.grid(row=3,column=3)
j= a.Button(b,activebackground="green" , bg="light green" ,text="7", width=5)
j.grid(row=4,column=1)
k= a.Button(b,activebackground="red" , bg="orange" ,text="8", width=5)
k.grid(row=4,column=2)
l= a.Button(b,activebackground="indigo" , bg="violet" ,text="9", width=5)
l.grid(row=4,column=3)
m= a.Button(b,activebackground="brown" , bg="pink" ,text="0", width=5)
m.grid(row=5,column=1)
n= a.Button(b,bg="black" ,text="+", font="times" , fg="yellow", width=4)
n.grid(row=5,column=2)
o= a.Button(b,bg="black" ,text="-",font="times" ,fg="yellow", width=4)
o.grid(row=5,column=3)
p= a.Button(b,bg="black" ,text="*",font="times", fg="yellow", width=4)
p.grid(row=5,column=4)
q= a.Button(b,bg="black"  ,text="/",font="times", fg="yellow", width=4)
q.grid(row=3,column=4)
r= a.Button(b,activebackground="white" , bg="blue" ,text="=", width=5)
r.grid(row=2,column=4)
r= a.Button(b, bg="blue" ,text="x*x", width=5)
r.grid(row=4,column=4)
b.mainloop()
 
