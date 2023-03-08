from tkinter import Tk, Button, Frame, messagebox, Label, Entry
from verificar import *
from generar import *

def ver():
    va.verif(verifi.get())
va = verificar ()
def gener():
    gene.gen(longitud.get(), caracteres.get())
gene = generar ()
ventana = Tk()
ventana.title("Generador de contrasenas")
ventana.geometry("600x400")
seccion1 = Frame(ventana, bg = "#00E8FF")
seccion1.pack(expand=True, fill="both")
bienvenida = Label(seccion1, text="Generador de contrasenas", bg="#26EAFD", font="consolas 20 bold")
bienvenida.pack()
correo = Label(seccion1, text="Longitud:", font="Arial 12", bg="#26EAFD")
correo.place(x=255, y=60)
contraseña = Label(seccion1, text="Caracteres especiales:", font="Arial 12", bg="#26EAFD")
contraseña.place(x=157, y=90)
verificacion = Label(seccion1, text="Contraseña:", font="Arial 12", bg="#26EAFD")
verificacion.place(x=235, y=120)
longitud= Entry(seccion1)
longitud.place(x=330, y=60)
caracteres = Entry(seccion1)
caracteres.place(x=330, y=90)
verifi= Entry(seccion1)
verifi.place(x=330, y=120)
seccion2 = Frame(ventana, bg = "orange")
seccion2.pack(expand=True, fill="both")

botonGenerar = Button(seccion2, text="Generar", fg="black", bg="white", font="Arial 12", command=gener)
botonVerificar = Button(seccion2, text="Verificar", fg="black", bg="white", font="Arial 12", command=ver)
botonGenerar.pack()
botonVerificar.pack()

ventana.mainloop() 