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
            messagebox.showwarning("Aguas", "Revisa tu formulario")
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
            messagebox.showwarning("Cuidado estimado usuario", "El id esta vacio, escribe uno valido")
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
            