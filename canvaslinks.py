##########################
# by Robin Deatherage 2014
##########################


"""
TO USE THIS CLICK THE BAR LINE AND
THE CLICK TEXT THEN SEE THE PYTHON SHELL OUTPUTS
"""
from tkinter import * 

def onObjectClick(event):                  
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))

root = Tk()

w = Canvas(root, width=900, height=700)

w.create_rectangle(0, 50, 50, 600)

obj1Id = w.create_line(300, 30, 100, 30, width=5, tags="obj1Tag")
obj2Id = w.create_text(300, 70, text='Click', tags='obj2Tag')

w.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick)       
w.tag_bind('obj2Tag', '<ButtonPress-1>', onObjectClick)   
print('obj1Id: ', obj1Id)
print('obj2Id: ', obj2Id)

w.pack()
root.mainloop()
