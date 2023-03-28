from tkinter import *
from tkinter import  ttk
import tkinter as tk
from ControladorPiplot import *  #Le presentamos la clase a la ventana

#Crear un objeto de tipo controlador

controlador = controladorPBD()

#Proceder a guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNomb.get(), varDesc.get(), varIni.get(), varFin.get())
    

Ventana = Tk()
Ventana.title("PIPLOT")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

#Aqui empieza Formulario Usuarios

titulo = Label(pestana1,text="Registro de Tareas", fg="Black", font=("Arial Black",18)).pack()

varNomb = tk.StringVar()
lblNomb = Label(pestana1, text="Nombre: ").pack()
txtNomb = Entry(pestana1,textvariable=varNomb).pack()

varDesc = tk.StringVar()
lblDesc = Label(pestana1, text="Descripcion: ").pack()
txtDesc = Entry(pestana1,textvariable=varDesc).pack()

varIni = tk.StringVar()
lblIni = Label(pestana1, text="Fecha Inicio: ").pack()
txtIni = Entry(pestana1,textvariable=varIni).pack()

varFin = tk.StringVar()
lblFin = Label(pestana1, text="Fecha Inicio: ").pack()
txtFin = Entry(pestana1,textvariable=varFin).pack()

btnGuardar = Button(pestana1, text="Guardar Tarea: ", command=ejecutaInsert).pack()

panel.add(pestana1, text="Registro de tareas")
panel.add(pestana2, text="Tareas")
panel.add(pestana3, text="Eliminar Tarea")
panel.add(pestana4, text="Actualizar Tarea")


Ventana.mainloop()