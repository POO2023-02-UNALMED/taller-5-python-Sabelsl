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
                
    def setListado(listado):
        Pez._listado = listado
        
    def getListado():
        return Pez._listado
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @staticmethod
    def crearSalmon(nombre, edad, genero=None):
        salmon = Pez(nombre, edad, "oceano", genero, "rojos", 6)
        Pez.salmones += 1
        return salmon
    
    @staticmethod
    def crearBacalao(nombre, edad, genero=None):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return bacalao
    
    
    def cantidadPeces():
        return len(Pez._listado)