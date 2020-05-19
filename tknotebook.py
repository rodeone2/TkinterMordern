"""
----------------------------------------------
   NoteBook Widget Example by Robin Deatherage
----------------------------------------------
"""

from tkinter import *
from tkinter import ttk

root = Tk()
lb1=Button(root, text='Search', command=root.destroy)#.pack(side=LEFT)
lb2=Entry(root, relief=SUNKEN)#.pack(padx=0, pady=0, side=LEFT)
#lb3=Button(root, text='Exit', command=root.destroy)
lb1.pack(padx=20, pady=0, fill=X)#, side=TOP)
lb2.pack(padx=20, pady=0, fill=X)#, side=TOP)
#lb3.pack(padx=90, pady=0, fill=X)#, side=TOP)
#Button(tab2, text='help', command=root.destroy).pack(padx=100, pady=100)
#im1=PhotoImage(file="img/project.png")
#im=im1
note = ttk.Notebook(root, width="1360")
tab1 = Frame(note,bd=5)
tab2 = Frame(note,bd=5)
tab3 = Frame(note,bd=5)

note.add(tab1, text="Tab One")#, image=im)#, compound=TOP)

tx1=Text(tab1, width=120, height=20)# sized in chars not pixels---xxx
tx1.pack()
tx1.insert("end", "a tEXT wIDGET")

note.add(tab2, text = "Tab Two")

note.add(tab3, text = "Tab Three")

note.pack()

# LETS FILL EACH TAB WITH WIDGETS--------XXX
bt1=Button(tab1, text="In Tab 1")
bt1.pack()
lb1=Label(tab1, text="In Tab 1")
lb1.pack()

bt1=Button(tab2, text="In Tab 2")
bt1.pack()
lb1=Label(tab2, text="In Tab 2")
lb1.pack()


bt1=Button(tab3, text="In Tab 3")
bt1.pack()
lb1=Label(tab3, text="In Tab 3")
lb1.pack()
root.mainloop()
