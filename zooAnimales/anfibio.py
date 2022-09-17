from animal import Animal
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

    def crearTana(self,nombre,edad,genero):
        Anfibio.ranas+=1
        return Anfibio(colorPiel="rojo",venenoso=True,habitat="selva",nombre=nombre,edad=edad,genero=genero)
    
    def crearSalamandra(self,nombre,edad,genero):
        Anfibio.salamandras+=1
        return Anfibio(colorPiel="negro y amarillo",venenoso=False,habitat="selva",nombre=nombre,edad=edad,genero=genero)

