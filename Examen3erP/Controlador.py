from tkinter import messagebox
import sqlite3


class controlador:
    
    def __init__(self):
        pass
    #Conexion a base de datos
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/lenovo/Desktop/BDImportaciones.db")
            print("Conexion exitosa")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def Registrar(self, Mercancia, Pai):
        
        conx = self.conexionBD()
        
        if(Mercancia == "" or Pai == ""):
            messagebox.showwarning("Error", "Campos vacios")
            conx.close()
        else:
            cursor = conx.cursor()
            qrInsert="insert into TB_Europa(Mercancia,Pais) values(?,?)"
            cursor.execute(qrInsert)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se registro con exito")