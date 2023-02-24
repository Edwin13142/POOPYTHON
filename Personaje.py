class Personaje:
    
    #Definimos el constructor del personaje 
    def __init__(self,esp,nom,alt):
    #Encapsulamos nuestros atributos
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
    #metodos del personaje
    #Nombramos de nueva forma nuestros atributos de la nueva manera que los modificamos
    def correr(self, status):
        if(status):
            print("El personaje "+self.__nombre+ " esta corriendo")
        else:
            print("El personaje "+self.__nombre+ " se detuvo")
    def lanzargranadas(self):
        print("El personaje "+self.__nombre+ " lanzo una granada")
    def recargararma(self, municiones):
        cargador = 10
        cargador = cargador+municiones
        print("El arma tiene "+str (cargador)+ " balas")
    def __pensar(self):
        print("Estoy pensando :((( ")
    
    #Declarar Getters & Setters de atributos
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nom):
        self.__nombre = nom
    def getEspecie(self):
        return self.__especie
    def setEspecie(self, esp):
        self.__especie = esp
    def getAltura(self):
        return self.__altura
    def setAltura(self, alt):
        self.__altura = alt