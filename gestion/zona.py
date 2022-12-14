class Zona:
    def __init__(self,nombre=None,zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
    
    def agregarAnimales(self,animal):
        self._animales.append(animal)
        animal.setZona(self)

    def cantidadAnimales(self):
        return len(self._animales)
    
    def setZoo(self,zoo):
        self._zoo=zoo
    
    def getZoo(self):
        return self._zoo

    def getNombre(self):
        return self._nombre