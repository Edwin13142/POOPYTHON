
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
#Ejemplo del Set para 1 atributo
heroe.setNombre(" Pepe Pecas ")


print("----------Datos heroe----------")
print("El personaje se llama: "+heroe.getNombre())
print("Pertenece a la especie: "+heroe.getEspecie())
print("Tiene una altura de: "+str(heroe.getAltura()))
heroe.correr(True)
heroe.lanzargranadas()
heroe.recargararma(recargaH)
#Ejemplo de un metodo privado
#heroe.__pensar()

print("----------Datos Villano----------")
print("El personaje se llama: "+villano.getNombre())
print("Pertenece a la especie: "+villano.getEspecie())
print("Tiene una altura de: "+str(villano.getAltura()))
villano.correr(False)
villano.lanzargranadas()
villano.recargararma(recargaV)
