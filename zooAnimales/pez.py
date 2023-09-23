from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)
        
    def setListado(self,listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def crearSalmon(self, nombre, edad, genero=None):
        salmon = Pez(nombre, edad, "oceano", genero, "rojos", 6)
        Pez._listado.append(salmon)
        Pez.salmones += 1
        return Pez.salmones
    
    def crearBacalao(self, nombre, edad, genero=None):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez._listado.append(bacalao)
        Pez.bacalaos += 1
        return Pez.bacalaos
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)