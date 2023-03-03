from tkinter import Tk, Button, Frame, messagebox, Label, Entry
from validacion import *
def validar():
    Validacion.validar_datos(correoI.get(), contraseñaI.get())
Validacion= validacion()  
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("600x400")
seccion1 = Frame(ventana, bg = "#00E8FF")
seccion1.pack(expand=True, fill="both")
bienvenida = Label(seccion1, text="Inicio de sesion", bg="#26EAFD", font="consolas 20 bold")
bienvenida.pack()
correo = Label(seccion1, text="Correo:", font="Arial 12", bg="#26EAFD")
correo.place(x=190, y=60)
contraseña = Label(seccion1, text="Contraseña:", font="Arial 12", bg="#26EAFD")
contraseña.place(x=157, y=90)
correoI= Entry(seccion1)
correoI.place(x=260, y=60)
contraseñaI = Entry(seccion1)
contraseñaI.config(show="*")
contraseñaI.place(x=260, y=90)
#2.- Agregamos los frames

seccion2 = Frame(ventana, bg= "white")
seccion2.pack(expand=True, fill="both")

#Instancia
#Validacion.validar_datos(correoI, contraseñaI) 

botonLogin = Button(seccion2, text="Login", fg="black", bg="white", font="Arial 12", command= validar)
botonLogin.pack()

ventana.mainloop()   