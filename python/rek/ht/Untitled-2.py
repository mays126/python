
from tkinter import *
from tkinter import messagebox
import random
from tkinter import font

def no():
    messagebox.showinfo(' ', 'Так и знал')
    quit()

def MotivationMouse(event):
    btnn.place(x = random.randint(0,500), y= random.randint(0,500))

root = Tk()
root.geometry('600x600')
root.title('Опрос')
root.resizable(width= False, height= False)

Label = Label(root, text= 'Да', font= 'Arial 20 bold', bg= 'white').pack()
btnn = Button(root, text= 'Да', font = 'Arial 20 bold')
btnn.place(x = 170, y = 100)

btny = Button(root, text= 'Да', font= 'Arial 20 bold', command=no).place(x= 350, y =100)

root.mainloop()
