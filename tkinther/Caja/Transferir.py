from tkinter import Tk, Button, Frame, messagebox, Label, Entry
class Transferir:
    def __init__(self):
        self.__Nocuenta = []
        self.__Titularr = []
        self.__edad = []
        self.__Saldo = []
    
    def registrar_usuario(self,Nocuenta,Titularr,edad,Saldo):
        self.__Nocuenta.append(Nocuenta)
        self.__Titularr.append(Titularr)
        self.__edad.append(edad)
        self.__Saldo.append(Saldo)
        
        messagebox.showinfo("Exito","Registro exitoso")
    
    def consultar_saldo(self, Nocuenta):
        if Nocuenta in self.__Nocuenta:
            index = self.__Nocuenta.index(Nocuenta)
            saldo = self.__Saldo[index]
            messagebox.showinfo("Consulta de Saldo","Tu saldo es: "+ str(saldo))
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")
    
    def ingresar_efectivo(self, Nocuenta, ingreso):
        if Nocuenta in self.__Nocuenta:
            index = self.__Nocuenta.index(Nocuenta)
            saldo = self.__Saldo[index]
            saldo += ingreso
            self.__Saldo[index] = saldo
            messagebox.showinfo("Actualización de saldo","Tu saldo es:"+ str(saldo))
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")
    
    def retirar_efectivo(self, Nocuenta, retiro):
        if ncuenta in self.__Nocuenta:
            index = self.__Nocuenta.index(Nocuenta)
            saldo = self.__Saldo[index]
            if saldo >= retiro:
                saldo -= retiro
                self.__Saldo[index] = saldo
                messagebox.showinfo("Actualización de saldo","Tu saldo es:"+ str(saldo))
            else:
                messagebox.showerror("Error", "No tienes suficiente saldo")
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")
    
    def depositar_a_otra_cuenta(self, cuentao, cuentad, deposito):
        if cuentao in self.__Nocuenta and cuentad in self.__Nocuenta:
            index_origen = self.__Nocuenta.index(cuentao)
            index_destino = self.__Nocuenta.index(cuentad)
            saldo_origen = self.__Saldo[index_origen]
            saldo_destino = self.__Saldo[index_destino]
            if saldo_origen >= deposito:
                saldo_origen -= deposito
                saldo_destino += deposito
                self.__Saldo[index_origen] = saldo_origen
                self.__Saldo[index_destino] = saldo_destino
                messagebox.showinfo("Depósito completado","Tu nuevo saldo es:"+ str(saldo_origen))
            else:
                messagebox.showerror("Error", "No tienes suficiente saldo")
        else:
            messagebox.showerror("Error", "No se encontró la cuenta")