from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    #Preparamos la conexion a la base de datos para usarla cuando se ocupe
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/lenovo/Desktop/Usuarios2.db")
            print("Conexion exitosa")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardarUsuario(self,cor,con,nom):
        
        #1.- Llamar a la conexion
        conx = self.conexionBD()
        
        #2.- Revisar parametros vacios
        
        if(nom == "" or cor == "" or con == ""):
            messagebox.showerror("Error", "Revisa tu formulario")
            conx.close()
        else:
            #3.- Preparar datos y el querySQL
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (cor,conH,nom)
            qrInsert="insert into TBRregistrados(correo,contra,nombre) values(?,?,?)"
            
            #4.- Proceder a Insertar y cerramos la base de datos
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se guardo el usuario")
    
    def encriptarCon(slef,con):
        conPlana = con
        conPlana = conPlana.encode() #onvierte la contraseña a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana, sal)
        return conHa
    
    def consultarUsuario(self,id):
        #1.- Preparar la conexion
        
        conx= self.conexionBD()
        
        #2.- Verificar que el Id no este vacio
        
        if(id == ""):
            messagebox.showwarning("Error", "El id esta vacio, escribe uno valido")
            conx.close()
        else:
            #3.- Proceder a buscar el usuario
            try:
                #4.- Preparar lo necesario para el select
                cursor=conx.cursor()
                sqlSelect = "select * from TBRregistrados where id="+id
                
                #5.- Ejecucion y guardado de la consulta
                
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error en la consulta")
    
    def consulta(self):
        #1.- Preparamos nuestra conexion a base de datos
        
        conx =self.conexionBD()
        try:
            #Preparamos el select
            cursor = conx.cursor()
            sqlSelect = "select * from TBRregistrados"
            #Ejecutamos la consulta
            cursor.execute(sqlSelect)
            RSusuario = cursor.fetchall()
            conx.close()
                
            return RSusuario
                
        except sqlite3.OperationalError:
            print("Error en la consulta")
            
    def actualiza(self, idd, corr, cont, nom):
        
        #1.- Preparamos nuestra base de datos
        conx = self.conexionBD()
        
        #Revisamos campos
        
        if(nom == "" or corr == "" or cont == "" or idd ==""):
            messagebox.showerror("Error", "Revisa tu formulario")
            conx.close()
        else:
        
            try:
                #Preparamos el update
                cursor = conx.cursor()
                conH = self.encriptarCon(cont)
                sqlUpdate = ("UPDATE TBRregistrados SET correo = ?, contra = ?, nombre = ? WHERE id = ?")
                datos = (corr,conH,nom,idd)
                cursor.execute(sqlUpdate, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Se actualizo el usuario")
            
            except sqlite3.OperationalError:
                print("Error en la consulta")
            
    def eliminar(self,idd):
        
        #1.- Preparamos la conexion
        conx = self.conexionBD()
        
        if(idd == ""):
            messagebox.showerror("Error", "Revisa tu formulario")
            conx.close()
        
        else:
        
            try: 
                #Preparamos el eliminar
                cursor = conx.cursor()
                sqlDelete = ("DELETE FROM TBRregistrados WHERE id = ?")
                datos = (idd)
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