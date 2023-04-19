from tkinter import *
from tkinter import  ttk
import tkinter as tk
from Controlador import * 

control = controlador ()

def registrar():
    controlador.Registrar(varMer.get(), varPai.get())

Ventana = Tk()
Ventana.title("Importaciones")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

#Programacion de registro

bienvenida = Label(pestana1,text="Registrar Mercancia", fg="Black", font=("Arial Black",18)).pack()

varMer = tk.StringVar()
lblMer = Label(pestana1, text="Mercancia: ").pack(pady=5)
txtMer = Entry(pestana1,textvariable=varMer).pack(pady=5)

varPai = tk.StringVar()
lblPais = Label(pestana1, text="Pais: ").pack(pady=5)
txtPais = Entry(pestana1,textvariable=varPai).pack(pady=5)

btnRegistrar = Button(pestana1,text="Registrar", bg="Orange", command=registrar).pack(pady=5)

#Programacion de eliminar

texto = Label(pestana2,text="Formulario para eliminar", fg="Black", font=("Arial Black",18)).pack()

varID = tk.StringVar()
lblID = Label(pestana2, text="ID: ").pack(pady=5)
txtID = Entry(pestana2,textvariable=varID).pack(pady=5)

btnEliminar = Button(pestana2,text="Eliminar", bg="Red", fg="White").pack(pady=5)

#Programacion de consulta

texto2 = Label(pestana3,text="Consulta por pais", fg="Black", font=("Modern",18)).pack()

varBus = tk.StringVar()
lblPas= Label(pestana3, text="Ingresa el pais: ").pack()
txtPas = Entry(pestana3,textvariable=varBus).pack()
btnBusqueda = Button(pestana3,text="Buscar").pack()

subBus = Label(pestana3,text="Registrado:",fg="Black",font=("Modern",18)).pack()
textBus = tk.Text(pestana3,height=5,width=52)
textBus.pack()


panel.add(pestana1, text="Insertar:")
panel.add(pestana2, text="Eliminar:")
panel.add(pestana3, text="Consulta por pais:")

Ventana.mainloop()