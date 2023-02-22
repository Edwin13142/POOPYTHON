
from Personaje import *

#1.-Solicitar datos
print("----------------Datos heroe------------------")
especieH = input("Escribe el especie del Heore:")
nombreH = input("Escribe el nombre del Heroe:")
alturaH = float(input("Escribe la altura del Heroe:"))
recargaH = int(input("Cuantas balas recargas al Heroe:"))
print("----------------Datos Villano----------------")
especieV = input("Escribe el especie del Villano:")
nombreV = input("Escribe el nombre del Villano:")
alturaV = float(input("Escribe la altura del Villano:"))
recargaV = int(input("Cuantas balas recargas al Villano:"))
#2.- Crear un objeto de la clase personaje 

heroe = Personaje(especieH,nombreH,alturaH)
villano = Personaje(especieV,nombreV,alturaV)

#3.- Usar atributos y metodos
print("----------Datos heroe----------")
print("El personaje se llama: "+heroe.nombre)
print("Pertenece a la especie: "+heroe.especie)
print("Tiene una altura de: "+str(heroe.altura))
heroe.correr(True)
heroe.lanzargranadas()
heroe.recargararma(recargaH)
print("----------Datos Villano----------")
print("El personaje se llama: "+villano.nombre)
print("Pertenece a la especie: "+villano.especie)
print("Tiene una altura de: "+str(villano.altura))
villano.correr(False)
villano.lanzargranadas()
villano.recargararma(recargaV)
