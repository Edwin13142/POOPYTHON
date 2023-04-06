from tkinter import *
from tkinter import  ttk
import tkinter as tk

login = Tk()
login.title("Inicio de sesión")
login.geometry("925x500+300+200")
login.configure(bg="#fff")
login.resizable(False,False)

imagen = PhotoImage(file='C:/Users/lenovo/Desktop/login.png')
Label(login,image=imagen,bg="white").place(x=50, y=50)



login.mainloop()