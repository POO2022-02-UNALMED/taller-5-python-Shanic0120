from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorPiel=None,venenoso=False):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas+=1
        return Anfibio(colorPiel="rojo",venenoso=True,habitat="selva",nombre=nombre,edad=edad,genero=genero)
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        cls.salamandras+=1
        return Anfibio(colorPiel="negro y amarillo",venenoso=False,habitat="selva",nombre=nombre,edad=edad,genero=genero)

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso
