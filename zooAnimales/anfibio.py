from .animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)
        
        
        
    def setListado(listado):
        Anfibio._listado = listado
        
    def getListado():
        return Anfibio._listado
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def isVenenoso(self):
        return self._venenoso
    
    @staticmethod
    def crearRana(nombre, edad, genero=None):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @staticmethod
    def crearSalamandra(nombre, edad, genero=None):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)