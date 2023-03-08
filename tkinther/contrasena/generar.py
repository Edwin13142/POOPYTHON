from tkinter import messagebox
import random
class generar:
 
    def __init__(self):
        self.minus = "abcdefghijklmnñopqrstuvwxyz"
        self.mayus = self.minus.upper()
        self.num = "0123456789"
        self.general = self.minus+self.mayus+self.num
        self.general2 = self.minus
    def gen (self, longitud, caracteres):
        if caracteres == "Si":
            muestra = random.sample(self.general, longitud)
            contraseña = "".join(muestra)
            messagebox.showinfo("Contraseña", "Tu contraseña es:",contraseña)
        if caracteres == "No":
            muestra = random.sample(self.general2, longitud)
            contraseña = "".join(muestra)
            messagebox.showinfo("Contraseña", "Tu contraseña es:",contraseña)
            

        