from zooAnimales.animal import Animal
class Pez(Animal):
    _listado=[]
    salmones=0
    bacalaos=0

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorEscamas=None,cantidadAletas=0):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        Pez.salmones+=1
        return Pez(colorEscamas="rojo",cantidadAletas=6,habitat="oceano",nombre=nombre,edad=edad,genero=genero)
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        Pez.bacalaos+=1
        return Pez(colorEscamas="gris",cantidadAletas=6,habitat="oceano",nombre=nombre,edad=edad,genero=genero)

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def getColorEscamas(self):
        return self._colorEscamas