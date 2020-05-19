"""
DEVELOPE3D FOR PYTHON 3.7 PLUS BY ROBIN DEATHERAGE
WINDOWS 7,8,9 & 10
"""
from tkinter import *
import re
re.purge()
"""
class one():
    pass
def two():
    pass
print(type(one))
print(type(two))
"""

import binascii
import gzip
myfile="H4sIAAAAAAAA//NIzcnJVwjPL8pJAQBWsRdKCwAAAA=="
myfile=f"""{myfile}"""
xx=gzip.decompress(binascii.a2b_base64(myfile))
#print(xx)


"""
---------------
   COLOR SCHEME
---------------
"""
clrcn = "#323232"
clrfr = "#242424"
clrbl = "#0099ff"
clrbt = "#4f4f4f"
clrlb = "lightgrey"    

top= Tk()
top.state('zoomed')
wid = top.winfo_screenwidth()
hit = top.winfo_screenheight()
top.geometry(str(wid)+"x"+str(hit)+"+0+0")
top.title('Cleaner')
top.option_add("*Font", "TimesNewRoman 7")#"Helvetica 8")
#top.configure(font=("Times" "New Roman" "12" "bold"))
"""
-------------------------------------------------
   CANVAS SCROLLBAR AND PAGE LENGTH SCROLL REGION
-------------------------------------------------
"""
w=Canvas(top, bg='#323232', width=wid-22, height=hit, scrollregion=(0,0,400,18500))# XXX--SET HEIGHT HERE
hbar=Scrollbar(top,width=20,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=w.xview)
vbar=Scrollbar(top, width=20, orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=w.yview)
w.config(width=wid-22,height=hit-25)
#w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set, yscrollincrement='35')
w.pack(side=LEFT,expand=True,fill=BOTH)
"""
--------------
   TEXT EDITOR 
--------------
"""
# TEXT WIDGET EDITOR
tx=Text(w, width=70, height=32, bg='#000000', fg='grey',
        bd=2, relief=GROOVE, font=("Times", 11, "bold"),
        insertbackground='grey')
w.create_window(92, 35, window=tx, anchor=NW)
"""
----------
   TOOLBAR
----------
"""
# TOOLBAR
toolbar=Frame(w, width=1300, height=34, bg='#242424', bd=2, relief=GROOVE)
w.create_window(200, 5, window=toolbar, anchor=NW)

bt1 = Button (toolbar, text='Exit',
                  bg='#4f4f4f', fg='lightgrey',
                  command=top.destroy)
bt1.grid(row=0, column=0)

bt2=Button(toolbar, text='Info', bg='#4f4f4f', fg='lightgrey')
bt2.grid(row=0, column=1)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=2)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=3)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=4)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=5)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=6)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=7)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=8)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=9)

bt3=Button(toolbar, text='Help', bg='#4f4f4f', fg='lightgrey')
bt3.grid(row=0, column=10)

# POPUP BUTTON ICONS
im1 = PhotoImage(file="img/max.png")
im2 = PhotoImage(file="img/min.png")

# POPUP ONE
pop1=Frame(w, width=21, height=21, bg='#242424', bd=2, relief=GROOVE)
w.create_window(5, 5, window=pop1, anchor=NW)
# POPUP ONE
def pop_open1():
    pop2=Frame(w, width=100, height=500, bg='#242424', bd=2, relief=GROOVE)
    w.create_window(5, 5, window=pop2, anchor=NW)

    b0=Button(pop2, image=im2,
              bg='#4f4f4f',
              fg='lightgrey',
              text='File', width=25,
              compound=RIGHT,
              command=pop2.destroy)
    b0.pack(anchor=NW)#.grid(row=0, column=0, sticky=W)

    b1=Button(pop2, text='New File',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=1, column=0, sticky=W)

    b1=Button(pop2, text='Open',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=2, column=0, sticky=W)

    b1=Button(pop2, text='Save',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=3, column=0, sticky=W)

    b1=Button(pop2, text='SaveAs',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=4, column=0, sticky=W)

# OPENS POP_OPEN1    
pb1=Button(pop1, image=im1,
           bg='#4f4f4f',
           fg='lightgrey',
           text='File', width=25,
           compound=RIGHT,
           command=pop_open1)
pb1.grid(row=0, column=0)

# POPUP TWO    
pop3=Frame(w, width=100, height=500, bg='#242424', bd=2, relief=GROOVE)
w.create_window(42, 5, window=pop3, anchor=NW)
# POPUP TWO
def pop_open2():
    pop3=Frame(w, width=100, height=500, bg='#242424', bd=2, relief=GROOVE)
    w.create_window(42, 5, window=pop3, anchor=NW)

    b0=Button(pop3, image=im2,
              bg='#4f4f4f',
              fg='lightgrey',
              text='TkMethods',
              compound=RIGHT,
              command=pop3.destroy)
    b0.pack(anchor=NW)#.grid(row=0, column=0, sticky=W)

    b1=Button(pop3, text='Tk',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=1, column=0, sticky=W)

    b1=Button(pop3, text='Frame',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=2, column=0, sticky=W)

    b1=Button(pop3, text='Canvas',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=3, column=0, sticky=W)

    b1=Button(pop3, text='LabelFrame',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=4, column=0, sticky=W)

    b1=Button(pop3, text='PanedWindow',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=5, column=0, sticky=W)

    b1=Button(pop3, text='Text',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=5, column=0, sticky=W)

    b1=Button(pop3, text='Label',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=5, column=0, sticky=W)

    b1=Button(pop3, text='Button',
              bg='#4f4f4f',
              fg='lightgrey',)
    b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=5, column=0, sticky=W)
    
# OPENS POP_OPEN2
pb2=Button(pop3, image=im1,
           bg='#4f4f4f',
           fg='lightgrey',
           text='TkMethods',
           compound=RIGHT,
           command=pop_open2)
pb2.grid(row=0, column=0)


# LEFT MENU lm
lm=Frame(w, width=100, height=500, bg='#242424', bd=2, relief=GROOVE)
w.create_window(5, 65, window=lm, anchor=NW)
b1=Button(lm, text='Label',
              bg='#4f4f4f',
              fg='lightgrey',)
b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=5, column=0, sticky=W)

b1=Button(lm, text='Button',
          bg='#4f4f4f',
          fg='lightgrey',)
b1.pack(fill=BOTH, expand=1)#anchor=NW)#.grid(row=5, column=0, sticky=W)

# SLIDER SECTIONS sm
sm=Frame(w, width=400, height=600, bg='#242429', bd=2, relief=GROOVE)
w.create_window(660, 35, window=sm, anchor=NW)





"""# HORIZONTAL PANEL"""
m1 = PanedWindow(sm, bg="grey", width=400, height=514, sashwidth=3, showhandle=True)
m1.pack(fill=BOTH, expand=1)

#left = Label(m1, text="left pane")
#m1.add(left)

"""# VERTICAL PANEL"""
m2 = PanedWindow(m1, bg="grey", sashwidth=3, showhandle=True, orient=VERTICAL)
m1.add(m2)

f4 = LabelFrame(m1, text="Loops", bg='#242424', fg="white",
                width=100, height=60)
m2.add(f4)

f5 = LabelFrame(m1, text="Conditions", bg='#242424', fg="white",
                width=100, height=60)
m2.add(f5)

f6 = LabelFrame(m1, text="Generators", bg='#242424', fg="white",
                width=100, height=60)
m2.add(f6)

f7 = LabelFrame(m1, text="Try/Else", bg='#242424', fg="white",
                width=100, height=60)
m2.add(f7)

# F4 FRAME BUTTONS LOOPS
tp = Button(f4, text="For", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="For/In", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="For/Enumerate", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="For/Range", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="For/Map", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="For/Zip", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="While/Loop", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f4, text="While/True", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

# F5 FRAME BUTTONS CONDITIONS
tp = Button(f5, text="If", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f5, text="If/Else", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f5, text="If/Elif/Else", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

# F6 FRAME BUTTONS GENERATORS
tp = Button(f6, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f6, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f6, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f6, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f6, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f6, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

# F7 FRAME BUTTONS TRY/ELSE
tp = Button(f7, text="For", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f7, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f7, text="...", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

# MORE
f1 = LabelFrame(m1, text="Function", bg='#242424', fg="white",
                width=100, height=60)
f2 = LabelFrame(m1, text="Class", bg='#242424', fg="white",
                width=100, height=60)
f3 = LabelFrame(m1, text="Imports", bg='#242424', fg="white",
                width=100, height=60)
m1.add(f1), m1.add(f2), m1.add(f3)

# F7 FRAME BUTTONS TRY/ELSE
tp = Button(f1, text="Function", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f1, text="Function/Args", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

tp = Button(f1, text="Function/Return", bg='#4f4f4f', fg='white')
tp.pack(fill=X)

#-------------------------------------------------------
"""
   CANVAS AUTOSCROLL SCRIPT MUST REMAIN ABOVE MAINLOOP()
   SCROLL SPEED CAN BE ADJUSTED BY ALTERING
   yscrollincrement='35' LOCATED ABOVE
"""
#w.focus_set()

def rollWheel(event):
    direction = 0
    #event.widget.focus_set()
    if event.num == 5 or event.delta == -120:
     direction = 1
    if event.num == 4 or event.delta == 120:
     direction = -1
    event.widget.yview_scroll(direction, UNITS)

w.bind('<MouseWheel>', lambda event: rollWheel(event))
w.bind('<Button-4>', lambda event: rollWheel(event))
w.bind('<Button-5>', lambda event: rollWheel(event))    
top.mainloop()
