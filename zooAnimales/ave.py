from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        
        
        
        
    def setListado(listado):
        Ave._listado = listado
        
    def getListado():
        return Ave._listado
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas

    @staticmethod
    def crearHalcon(nombre, edad, genero=None):
        halcon = Ave(nombre, edad, "montanas", genero, "café glorioso")
        Ave.halcones += 1
        Ave._listado.append(halcon)
        return Ave.halcones
    
    @staticmethod
    def crearAguila(nombre, edad, genero=None):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        Ave._listado.append(aguila)
        return Ave.aguilas
    
    
    def cantidadAves():
        return len(Ave._listado)