from zooAnimales.animal import Animal
class Ave(Animal):
    _listado=[]
    halcones=0
    aguilas=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorPlumas=None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        cls.halcones+=1
        return Ave(colorPlumas="cafe glorioso",habitat="montanas",nombre=nombre,edad=edad,genero=genero)
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        cls.aguilas+=1
        return Ave(colorPlumas="blanco y amarillo",habitat="montanas",nombre=nombre,edad=edad,genero=genero)
