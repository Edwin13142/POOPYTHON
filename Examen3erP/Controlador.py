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
            
    def Registrar(self, Mercancia, Pais):
        
        conx = self.conexionBD()
        
        if(Mercancia == "" or Pais == ""):
            messagebox.showwarning("Error", "Campos vacios")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (Mercancia, Pais)
            qrInsert="insert into TB_Europa(Mercancia,Pais) values(?,?)"
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se registro con exito")
            
    def Eliminar(self, ID):
        
        conx = self.conexionBD()
        
        if(ID ==""):
            messagebox.showwarning("Error", "Campos vacios")
            conx.close()
        else:
            try:
                
                cursor = conx.cursor()
                sqlDelete = ("DELETE FROM TBR_Europa WHERE IDImpo = ?")
                datos = (ID)
                pregunta = messagebox.askokcancel("Confirmacion", "¿Deseas eliminar ese usuario?")
                if pregunta == True:
                    cursor.execute(sqlDelete,datos)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito", "Se elimino el usuario")
                else:
                    conx.close()
                    messagebox.showerror("Error", "El Usuario no fue eliminado")
                    
            except sqlite3.OperationalError:
                print("Error en la consulta")
                
    def Consulta(self, Pais):
        
        conx = self.conexionBD()
        
        if(Pais ==""):
            messagebox.showwarning("Error", "Campos vacios")
            conx.close()
        else:
            try:
                cursor=conx.cursor()
                sqlSelect = "select * from TBR_Europa where Pais="+Pais
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error en la consulta")
        