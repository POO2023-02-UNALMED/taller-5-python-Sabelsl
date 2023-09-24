from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)
        

    def setListado(listado):
        Mamifero._listado = listado
        
    def getListado():
        return Mamifero._listado

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def isPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas

    @staticmethod
    def crearCaballo(nombre, edad, genero=None):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos +=1
        return caballo
    
    @staticmethod
    def crearLeon(nombre, edad, genero=None):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return leon
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)