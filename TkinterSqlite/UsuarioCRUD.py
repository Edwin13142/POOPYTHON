from tkinter import *
from tkinter import  ttk
import tkinter as tk
from ControladorBD import *  #Le presentamos la clase a la ventana

#Crear un objeto de tipo controlador

controlador = controladorBD()

#Proceder a guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varCor.get(), varCon.get(), varNomb.get())

#Funcion para buscar un usuario

def ejecutaSelectU():
    rsUsuario = controlador.consultarUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ usu[1] + " "+ str(usu[2])+ " "+ usu[3]
    if(rsUsuario):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showerror("Error","Usuario no encontrado")
        
def ejecutaConsultU():
    rsUsuario = controlador.consulta()
    tree.delete(*tree.get_children())
    for usu in rsUsuario:
        tree.insert("", "end",text=usu[0], values=(usu[1], usu[2], usu[3]))
    
def Actualizar():
    controlador.actualiza(barID.get(),barCor.get(), barCon.get(), barNom.get())
    
def Eliminar():
    controlador.eliminar(VARId.get())
    

Ventana = Tk()
Ventana.title("CRUD Usuarios")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#Aqui empieza Formulario Usuarios

titulo = Label(pestana1,text="Registro de Usuarios", fg="Blue", font=("Modern",18)).pack()

varNomb = tk.StringVar()
lblNomb = Label(pestana1, text="Nombre: ").pack()
txtNomb = Entry(pestana1,textvariable=varNomb).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ").pack()
txtCor = Entry(pestana1,textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text="Contraseña: ").pack()
txtCon = Entry(pestana1,textvariable=varCon).pack()

btnGuardar = Button(pestana1, text="Guardar usuario: ", command=ejecutaInsert).pack()

# Pestaña No. 2 de buscar usuario

titulo2 = Label(pestana2,text="Buscar Usuario", fg="Green", font=("Modern",18)).pack()

varBus = tk.StringVar()
lblid= Label(pestana2, text="Identificador de usuario: ").pack()
txtid = Entry(pestana2,textvariable=varBus).pack()
btnBusqueda = Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus = Label(pestana2,text="Registrado:",fg="blue",font=("Modern",18)).pack()
textBus = tk.Text(pestana2,height=5,width=52)
textBus.pack()

# Pestaña No.3 de buscar usuarios

Presentacion = Label(pestana3,text="Usuarios Registrados",fg="Black",font=("Arial",15)).pack()
tree = ttk.Treeview(pestana3)
tree['columns']=('correo', 'contraseña', 'nombre')
tree.column('#0', width=50, minwidth=50)
tree.column('correo', width=150, minwidth=150)
tree.column('nombre', width=120, minwidth=120)
tree.column('contraseña', width=100, minwidth=100)
tree.heading('#0', text='Id')
tree.heading('correo', text='Correo')
tree.heading('contraseña', text='Contraseña')
tree.heading('nombre', text='Nombre')
tree.pack()
btnBusquedas = Button(pestana3,text="Consultar",command=ejecutaConsultU).pack()

#Pesataña No.4 Actualizar usuario

tit = Label(pestana4,text="Actualizar Usuario",fg="Black",font=("Arial",15)).pack()

barID = tk.StringVar()
idLabel =  Label(pestana4,text="Id:",fg="Black",font=("Arial",15)).pack()
idEntry =  Entry(pestana4,textvariable=barID).pack()

barNom = tk.StringVar()
nomLabel =  Label(pestana4,text="Nombre:",fg="Black",font=("Arial",15)).pack()
nomEntry =  Entry(pestana4,textvariable=barNom).pack()

barCor = tk.StringVar()
corLabel =  Label(pestana4,text="Correo:",fg="Black",font=("Arial",15)).pack()
corEntry =  Entry(pestana4,textvariable=barCor).pack()

barCon = tk.StringVar()
conLabel =  Label(pestana4,text="Contraseña",fg="Black",font=("Arial",15)).pack()
conEntry =  Entry(pestana4,textvariable=barCon).pack()

btnActualizar = Button(pestana4,text="Actualizar", command=Actualizar).pack()

#Pestaña No.5 Eliminar

tit = Label(pestana5,text="Eliminar Usuario",fg="Black",font=("Arial",15)).pack()

VARId = tk.StringVar()
IDLabel =  Label(pestana5,text="Id:",fg="Black",font=("Arial",15)).pack()
IDEntry =  Entry(pestana5,textvariable=VARId).pack()

btnEliminar = Button(pestana5,text="Eliminar",command=Eliminar).pack()

panel.add(pestana1, text="Formulario de usuarios:")
panel.add(pestana2, text="Buscar usuario:")
panel.add(pestana3, text="Consultar usuarios:")
panel.add(pestana4, text="Actualizar usuario:")
panel.add(pestana5, text="Eliminar")

Ventana.mainloop()