from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def _init_(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super()._init_(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def crearSalmon(self, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojos", 6)
        salmones += 1
        return salmon
    
    def crearBacalao(self, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        bacalaos += 1
        return bacalao
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)