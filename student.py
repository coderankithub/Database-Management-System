# Frontend

from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="cadet blue")

        strID = StringVar()
        firstName = StringVar()
        lastName = StringVar()
        dob = StringVar()
        age = StringVar()
        gender = StringVar()
        address = StringVar()
        mobile = StringVar()

        mainFrame = Frame(self.root, bg="cadet blue")
        mainFrame.grid()

        titFrame = Frame(mainFrame, bd=2, padx=54, pady=8,
                         bg='Ghost white', relief=RIDGE)
        titFrame.pack(side=TOP)

        self.lbtit = Label(titFrame, font=('arial', 47, 'bold'),
                           text='Student Management Systems', bg='Ghost White')
        self.lbtit.grid()

        buttonFrame = Frame(mainFrame, bd=2, width=1350, height=70,
                            padx=18, pady=10, bg='Ghost White', relief=RIDGE)
        buttonFrame.pack(side=BOTTOM)

        dataFrame = Frame(mainFrame, bd=1, width=1300, height=400,
                          padx=20, pady=20, bg='cadet blue', relief=RIDGE)
        dataFrame.pack(side=BOTTOM)

        dataFrameleft = LabelFrame(mainFrame, bd=1, width=1000, height=600, padx=20,
                                   bg='Ghost White', relief=RIDGE, font=('arial', 20, 'bold'), text="Student Info\n")
        dataFrameleft.pack(side=LEFT)

        dataFrameRight = LabelFrame(mainFrame, bd=1, width=450, height=300, padx=31, pady=3,
                                    bg='Ghost White', relief=RIDGE, font=('arial', 20, 'bold'), text="Student Details\n")
        dataFrameRight.pack(side=RIGHT)

        # Labels and Entry Widget

        self.lbstdID = Label(dataFrameleft, font=(
            'arial', 20, 'bold'), text='Student ID', bg='Ghost White', pady=2, padx=2)
        self.lbstdID.grid(row=0, column=0, sticky=W)


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
