class Persona:
    pass
    #Definimos constructor
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    #Definimos metodos
    def descripcion(self):
        return "{} tiene {} ".format(self.nombre, self.año)
    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)
doctor = Persona("Edwin", 26)
print(doctor.descripcion())
print(doctor.comentario("Hola"))