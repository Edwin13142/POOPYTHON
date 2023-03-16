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
        anoMM = " "
        anoM  = "23"
        nombre = self.__nombre.upper()
        ano = self.__ano
        appP = self.__appP.upper()
        appM = self.__appM.upper()
        carrera = self.__carrera.upper()
        anoMM += carrera [0:3]
        anoMM += anoM
        anoMM += ano[2:4]
        anoMM += nombre [:1]
        anoMM += appP [0:3]
        anoMM += appM [0:3]
        n = random.randint(1, 999)
        anoMM += str((n))
        
        messagebox.showinfo("Exito","Su matricula es:"+ anoMM)