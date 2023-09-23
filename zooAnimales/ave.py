from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)
        
    def setListado(self,listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas

    def crearHalcon(self, nombre, edad, genero=None):
        halcon = Ave(nombre, edad, "montanas", genero, "café glorioso")
        Ave.halcones += 1
        Ave._listado.append(halcon)
        return Ave.halcones
    
    def crearAguila(self, nombre, edad, genero=None):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        Ave._listado.append(aguila)
        return Ave.aguilas
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)