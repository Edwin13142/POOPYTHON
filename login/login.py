from tkinter import Tk, Button, Frame, messagebox, Label, Entry

correoU = "edwinmorales12365@gmail.com"
contraseñaU ="JIJIJI"
#5.- Declaramos las funciones para los mensajes
def validar_datos():
    if correoU == correoI and contraseñaU == contraseñaI:
        messagebox.showinfo("Login", "Bienvenido, Ingreso con exito")
    else:
        messagebox.showerror("Error", "Tus datos son erroneos")
#1.- Instanciamos nuestra ventana 
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("600x400")
seccion1 = Frame(ventana, bg = "blue")
seccion1.pack(expand=True, fill="both")
bienvenida = Label(seccion1, text="Inicio de sesion")
bienvenida.pack()
correo = Label(seccion1, text="Correo:")
correo.place(x=205, y=60)
contraseña = Label(seccion1, text="Contraseña:")
contraseña.place(x=180, y=90)
correoI= Entry(seccion1)
correoI.place(x=260, y=60)
self.contraseñaI = Entry(seccion1)
self.contraseñaI.config(show="*")
self.contraseñaI.place(x=260, y=90)
#2.- Agregamos los frames

seccion2 = Frame(ventana, bg= "white")
seccion2.pack(expand=True, fill="both")

#3.- Agregamos botones

botonLogin = Button(seccion2, text="Login", fg="black", bg="white", command=validar_datos)
botonLogin.pack()

ventana.mainloop()   