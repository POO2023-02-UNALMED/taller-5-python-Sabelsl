

from .animal import Animal


class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        
        
        
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
        Anfibio._listado.append(rana)
        Anfibio.ranas += 1
        return Anfibio.ranas

    @staticmethod
    def crearSalamandra(nombre, edad, genero=None):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio._listado.append(salamandra)
        Anfibio.salamandras += 1
        return Anfibio.salamandras
    
  
    def cantidadAnfibios():
        return len(Anfibio._listado)