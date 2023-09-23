from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado = []
    caballos = 0
    _pelaje = False
    leones = 0
    _patas= 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)
        
    def setListado(self,listado):
        self._listado = listado
        
    def getListado(self):
        return self._listado

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def isPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas

    def crearCaballo(self, nombre, edad, genero=None):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        
        Mamifero._listado.append(caballo)
        
        Mamifero.caballos +=1
        return Mamifero.caballos
    
    def crearLeon(self, nombre, edad, genero=None):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero._listado.append(leon)
        Mamifero.leones += 1
        return Mamifero.leones
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)