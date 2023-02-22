class Personaje:
    
    #Definimos el constructor del personaje 
    def __init__(self,esp,nom,alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
    #metodos del personaje
    def correr(self, status):
        if(status):
            print("El personaje "+self.nombre+ " esta corriendo")
        else:
            print("El personaje "+self.nombre+ " se detuvo")
    def lanzargranadas(self):
        print("El personaje "+self.nombre+ " lanzo una granada")
    def recargararma(self, municiones):
        cargador = 10
        cargador = cargador+municiones
        print("El arma tiene "+str (cargador)+ " balas")