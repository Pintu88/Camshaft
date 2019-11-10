import sqlite3
from tkinter import *

class Student:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.mainWindow.title("Student Management System")
        self.mainWindow.geometry("700x400+150+70")
        self.mainWindow.configure(bg='white')

####### Add Frame for add student Detail
        addFrame = Frame(self.mainWindow, bd=6, relief='ridge')
        addFrame.place(x=0, y=0, width=240, height=300)



####### Show Frame for add student Detail
        showFrame = Frame(self.mainWindow, bd=6, relief='ridge')
        showFrame.place(x=388, y=0, width=310, height=300)



studentWindow = Tk()
myGui = Student(studentWindow)
canvas = Canvas(studentWindow, width=145, height=145, bg='white', bd='0')
canvas.pack()
canvas.place(relx=0.45, rely=0.15, anchor=CENTER)
img = PhotoImage(file="images.png")
canvas.create_image(0, 0, anchor=NW, image=img)
# studentWindow.attributes("-toolwindow", 1)
studentWindow.resizable(0,0)
studentWindow.mainloop()
