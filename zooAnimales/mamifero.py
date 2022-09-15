from animal import Animal
class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,pelaje=False,patas=0):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
