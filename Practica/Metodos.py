#Palabras que indican una accion o un comportamiento ejemplo: suma, resta etc
#class nombre de la clase:
    #def nombre del metodo (self):
    #self.nombre de la variable = algoritmo o valor especifico
class Matematica :
    def sumar(self):
        self.n1 = 2
        self.n2 = 3
#creamos objetos
s = Matematica()
#llamamos al metodo
s.sumar()
print(s.n1 + s.n2)
