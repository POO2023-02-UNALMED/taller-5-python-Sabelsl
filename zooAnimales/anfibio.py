

from zooAnimales.animal import Animal


class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)
        
    def setListado(self,listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def isVenenoso(self):
        return self._venenoso
    
    def crearRana(self, nombre, edad, genero=None):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio._listado.append(rana)
        Anfibio.ranas += 1
        return Anfibio.ranas

    def crearSalamandra(self, nombre, edad, genero=None):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio._listado.append(salamandra)
        Anfibio.salamandras += 1
        return Anfibio.salamandras
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)