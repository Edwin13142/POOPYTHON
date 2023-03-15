#metodos
class Ropa:
    def __init__(self):
        self.marca = "American"
        self.talla = "M"
        self.color = "Rojo"
camisa = Ropa()
print(camisa.talla)
print(camisa.marca)
print(camisa.color)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1+n2
        self.resta = n1-n2
        self.multiplicacion = n1*n2
        self.division = n1/n2
#Crear onjeto
#Dentro de los parametros poner las variables
operacion = Calculadora(2,3)
print(operacion.multiplicacion)
print(operacion.suma)
print(operacion.resta)