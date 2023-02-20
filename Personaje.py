class Personaje:

    #declaracion de atributos
    especie = "Humano"
    nombre = "Medio Metro"
    altura = "1.40"

    #metodos del personaje
    def correr(self, status):
        if(status):
            print("El personaje"+self.nombre+ "esta corriendo")
        else:
            print("El personaje"+self.nombre+ "se detuvo")
    def lanzargranadas(self):
        print("El personaje"+self.nombre+ "lanzo una granada")
    def recargararma(self, municiones):
        cargador = 10
        cargador = cargador+municiones
        print("El arma tiene"+cargador+ "balas")