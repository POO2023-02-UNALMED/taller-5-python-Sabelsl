class Zoologico:
    
    _zonas = []

    def __init__(self, nombre, ubicacion):
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
    
    def setZona(self,zona):
        self._zona = zona
        
    def getZona(self):
        return self._zona
    
    def cantidadTotalAnimales(self):
        sumaAnimalesZonas = 0
        
        """ for zona in self._zonas:
            print(zona.getN())
            print(zona.getAnimales())
            print("//////")
            sumaAnimales Zonas += len(zona.getAnimales())"""
        return len(self._zonas[0].getAnimales())
    
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)