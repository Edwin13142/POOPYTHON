from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, DISABLED
from Funciones import *

def geneMat():
    nombre = nombreI.get()
    appP = apellPI.get()
    appM = apellMI.get()
    carrera = carreraI.get()
    ano = anoI.get()
    mi_matricula= Funciones(nombre, appP, appM, carrera, ano)
    mi_matricula.generar_matricula()
    
    
ventana = Tk()
ventana.title("Generador de matricula")
ventana.geometry("600x400")
seccion1 = Frame(ventana, bg = "#DAF7A6")
seccion1.pack(expand=True, fill="both")
bienvenida = Label(seccion1, text="Inicio de sesion", bg="#DAF7A6", font="consolas 20 bold")
bienvenida.pack()
nombreE = Label(seccion1, text="Nombre:", font="Arial 12", bg="#DAF7A6")
nombreE.place(x=190, y=60)
apellP = Label(seccion1, text="Apellido Paterno:", font="Arial 12", bg="#DAF7A6")
apellP.place(x=157, y=90)
apellM = Label(seccion1, text="Apellido Materno:", font="Arial 12", bg="#DAF7A6")
apellM.place(x=157, y=120)
ano = Label(seccion1, text="Año de nacimiento:", font="Arial 12", bg="#DAF7A6")
ano.place(x=157, y=150)
carreraa = Label(seccion1, text="Carrera:", font="Arial 12", bg="#DAF7A6")
carreraa.place(x=157, y=180)
nombreI= Entry(seccion1)
nombreI.place(x=300, y=60)
apellPI = Entry(seccion1)
apellPI.place(x=300, y=90)
apellMI = Entry(seccion1)
apellMI.place(x=300, y=120)
anoI = Entry(seccion1)
anoI.place(x=300, y=150)
carreraI = Entry(seccion1)
carreraI.place(x=300, y=180)


botonMatricula = Button(seccion1, text="Generar matricula", fg="black", bg="white", font="Arial 12", command=geneMat)
botonMatricula.place(x=300, y=250)

ventana.mainloop()
