from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado = []
    caballos = 0
    leones = 0
    _patas= 0

    def _init_(self, nombre, edad, habitat, genero, pelaje, patas):
        super()._init_(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        self._listado.append(self)

    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas
    def getPatas(self):
        return self._patas

    def crearCaballo(self, nombre, edad, genero):
        caballos = Mamifero(nombre, edad, "pradera", genero, True, 4)
        caballos +=1
        return caballos
    
    def crearLeon(self, nombre, edad, genero):
        leones = Mamifero(nombre, edad, "selva", genero, True, 4)
        leones += 1
        return leones
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)