from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def _init_(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super()._init_(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        self._listado.append(self)
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    def getLargoCola(self):
        return self._largoCola

    def crearIguana(self, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        iguanas += 1
        return iguana
    
    def crearSerpiente(self, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        serpientes += 1
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)