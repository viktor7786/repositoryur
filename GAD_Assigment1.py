from tkinter import *

count=0
def klik3x( event ): 
    global count
    count += 1
    print("Detection of triple click {} times.".format(count))
win = Tk()

win.minsize(250,150)
win.configure(bg="grey")

label = Label( win, text="Klik 3X",bg="white",font=("Helvetica",10),height=1,width=8)
label.place(relx=0.5,rely=0.5,anchor="center")
label.bind( "<Triple-Button>", klik3x )

exit = Button(win, text="Exit", bg = "red",height=2,width=4,command=win.destroy)
exit.place(relx=1,anchor="ne")

win.mainloop()