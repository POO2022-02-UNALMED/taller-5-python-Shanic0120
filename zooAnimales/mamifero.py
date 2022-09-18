from zooAnimales.animal import Animal
class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,pelaje=False,patas=0):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos+=1
        return Mamifero(pelaje=True,patas=4,habitat="pradera",nombre=nombre,edad=edad,genero=genero)
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones+=1
        return Mamifero(pelaje=True,patas=4,habitat="selva",nombre=nombre,edad=edad,genero=genero)

    def getPatas(self):
        return self._patas

    def isPelaje(self):
        return self._pelaje
