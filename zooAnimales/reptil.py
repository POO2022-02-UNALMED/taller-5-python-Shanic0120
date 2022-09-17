from animal import Animal
class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorEscamas=None,largoCola=0):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def crearIguana(self,nombre,edad,genero):
        Reptil.iguanas+=1
        return Reptil(colorEscamas="verde",largoCola=3,habitat="humedal",nombre=nombre,edad=edad,genero=genero)
    
    def crearSerpiente(self,nombre,edad,genero):
        Reptil.serpientes+=1
        return Reptil(colorEscamas="blanco",largoCola=1,habitat="jungla",nombre=nombre,edad=edad,genero=genero)

