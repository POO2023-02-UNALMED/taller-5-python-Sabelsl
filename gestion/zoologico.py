class Zoologico:
    
    _Zonas = []
    _sumaAnimalesZonas = 0

    def _init_(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getUbicacion(self):
        return self._ubicacion

    @classmethod
    def cantidadTotalAnimales(self):
        for i in Zoologico._Zonas:
            Zoologico._sumaAnimalesZonas += len(i)
        return Zoologico._sumaAnimalesZonas
    
    def agregarZonas(self, zona):
        self._Zonas.append(zona)