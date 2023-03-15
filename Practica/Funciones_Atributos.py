#Funciones para atributos
class Persona:
    edad = 27
    nombre = "Edwin"
    pais = "Brasil"
#Crear objeto

doctor = Persona()

print("la edad es:",doctor.edad)
print("La edad es:", getattr(doctor,"edad"))
#Para compronar si hay un atributo
print("El doctor tiene una edad?",hasattr(doctor, "edad"))
#Funcion para hacer cambios
print("Antes era:",doctor.nombre)
setattr(doctor, "nombre", "Juan")
print("Ahora es:",doctor.nombre)
#Para eliminar atributo
delattr(Persona, "pais")
print(doctor.pais)