from mamifero import Mamifero

class Animal:
    _totalAnimales=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales=Animal._totalAnimales+1
    
    @classmethod
    def totalPorTipo(cls):
        return 'Mamiferos: %s\nAves: %s\nReptiles: %s\nPeces: %s\nAnfibos: %s'%(Mamifero.cantidadMamiferos(),2,3,4,5)

    def setZona(self,zona):
        self._zona=zona


a=Animal()

print(a.totalPorTipo())