from tkinter import messagebox
import random
import numbers

class Funciones:
    
    def __init__(self, nombre, appP, appM, carrera, ano):
        self.__nombre = nombre
        self.__ano = ano
        self.__appP = appP
        self.__appM = appM
        self.__carrera = carrera
        
    def generar_matricula(self):
        anoM  = 23
        nombre = self.__nombre
        ano = self.__ano
        appP = self.__appP
        appM = self.__appM
        carrera = self.__carrera
        
        anoM += ano[2:4]
        anoM += nombre [:1]
        anoM += appP [:1]
        anoM += appM [:1]
        
        n1 = random.randint(1, 999)
        anoM += str((n1))
        anoM += carrera [0:3]
        
        messagebox.showinfo("Exito","Su matricula es:", anoM)