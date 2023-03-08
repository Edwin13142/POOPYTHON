from tkinter import messagebox
class verificar:
    def __init__(self):
        self.largo = False
        self.mayus = False
        self.num = False
    def verif(self, verifi):
        if len(verifi)>8:
            self.largo = True
        for i in range(len(verifi)):
            if verifi[i].isupper():
                self.mayus = True
            if verifi[i].isnumeric():
                self.num = True
        if self.largo and self.mayus and self.num:
            messagebox.showinfo("Exito", "La contraseña tiene buena seguridad")
        else:
            messagebox.showerror("Error", "La contraseña no es segura")