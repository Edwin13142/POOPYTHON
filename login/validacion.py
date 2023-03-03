from tkinter import messagebox
class validacion:
    
    def __init__(self):
        self.__correoU = "edwinmorales12365@gmail.com"
        self.__contraseñaU = "JIJIJI"
        

    def validar_datos(self,correoI,contraseñaI):
        if self.__correoU == correoI and self.__contraseñaU == contraseñaI: 
            messagebox.showinfo("Login", "Bienvenido, Ingreso con exito")
        else:
            messagebox.showerror("Error", "Tus datos son erroneos")