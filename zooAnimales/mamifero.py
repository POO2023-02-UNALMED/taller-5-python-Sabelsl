from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

        self._pelaje = False

        self._patas= 0
        

        
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
        
        Mamifero._listado.append(caballo)
        
        Mamifero.caballos +=1
        return Mamifero.caballos
    
    @staticmethod
    def crearLeon(nombre, edad, genero=None):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero._listado.append(leon)
        Mamifero.leones += 1
        return Mamifero.leones
    
    def cantidadMamiferos():
        return len(Mamifero._listado)