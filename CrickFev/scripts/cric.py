from tkinter import *
from levent import *
import tkinter.messagebox

def leftclick(self,event):
	tkinter.messagebox.showinfo('Live Score', tableData[self])

n=len(tableHeads)
matches={}
for i in range(n):
	matches[i]=str(tableHeads[i].h2.text)
	#print(tableData[i])


class Buttons:

	def __init__(self,master):
		getLiveEvents()
		frame=Frame(master)
		frame.pack()
		#label=Label(frame,text="Live Events",fg="red",sticky=E)
		#label.grid()
		for i in range(n):
			button=Button(frame,text=matches[i],fg="blue")
			button.bind("<Button-1>", lambda :leftclick(i))
			button.grid(columnspan=5,sticky=W)
		

		
        

             
        


  



root = Tk()

b = Buttons(root)
root.mainloop()

