from animal import Animal
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

    def crearCaballo(self,nombre,edad,genero):
        Mamifero.caballos+=1
        return Mamifero(pelaje=True,patas=4,habitat="pradera",nombre=nombre,edad=edad,genero=genero)
    
    def crearLeon(self,nombre,edad,genero):
        Mamifero.leones+=1
        return Mamifero(pelaje=True,patas=4,habitat="selva",nombre=nombre,edad=edad,genero=genero)

