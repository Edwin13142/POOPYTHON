from tkinter import Tk,Button,Frame, messagebox

def mostrarMensajes():
    messagebox.showinfo("Aviso","Presionaste el boton azul") #Definimos la funcion para mostrar un mensaje
    
#1.- Instanciamos el objeto ventana 
ventana = Tk()
ventana.title("Practica 11") # Titulo para mi ventana
ventana.geometry("600x400") # Tamaño de mi ventana 

#2.- agregamos los Frames

seccion1 = Frame(ventana, bg="red") #Especificar siempre a donde debe de ir 
seccion1.pack(expand=True, fill='both') #Posicionamos dentro del pack
seccion2 = Frame(ventana, bg="orange") #Especificar siempre a donde debe de ir 
seccion2.pack(expand=True, fill='both') #Posicionamos dentro del pack
seccion3 = Frame(ventana, bg="blue") #Especificar siempre a donde debe de ir 
seccion3.pack(expand=True, fill='both') #Posicionamos dentro del pack

#3.- Agregamos botones
botonAzul = Button(seccion1, text="Boton Azul", fg="blue", command=mostrarMensajes)
botonAzul.place(x=260, y=60)
botonNegro = Button(seccion2, text="Boton Negro", fg="white", bg="black")
botonNegro.grid(row=0, column=0)
botonAmarillo = Button(seccion2, text="Boton Amarillo", bg="#ffff4d")
botonAmarillo.grid(row=1, column=1)
botonVerde = Button(seccion3, text="Boton Verde", bg="green")
botonVerde.configure(height=1, width=10)
botonVerde.pack()


#llamamos al Main

ventana.mainloop() #Siempre debe de ir al final del codigo