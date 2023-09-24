from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

        
    def setListado(listado):
        Reptil._listado = listado
        
    def getListado():
        return Reptil._listado
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
        
    def getLargoCola(self):
        return self._largoCola

    @staticmethod
    def crearIguana(nombre, edad, genero=None):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil._listado.append(iguana)
        Reptil.iguanas += 1
        return Reptil.iguanas
   
    @staticmethod
    def crearSerpiente(nombre, edad, genero=None):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil._listado.append(serpiente)
        Reptil.serpientes += 1
        return Reptil.serpientes


    def cantidadReptiles():
        return len(Reptil._listado)