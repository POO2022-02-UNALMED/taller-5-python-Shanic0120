class Animal:
    _totalAnimales=0
    def __init__(self,nombre=None,edad=0,habitat=None,genero=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales=Animal._totalAnimales+1

    def toString(self):
        if self._zona!=None:
            return "Mi nombre es %s, tengo una edad de %s, habito en %s y mi genero es %s, la zona en la que me ubico es %s, en el %s"%(self._nombre,self._edad,self._habitat,self._genero,self._zona,self._zona.getZoo())
        else:
            return "Mi nombre es %s, tengo una edad de %s, habito en %s y mi genero es %s"%(self._nombre,self._edad,self._habitat,self._genero)


    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        return 'Mamiferos: %s\nAves: %s\nReptiles: %s\nPeces: %s\nAnfibos: %s'%(Mamifero.cantidadMamiferos(),Ave.cantidadAves(),Reptil.cantidadReptiles(),Pez.cantidadPeces(),Anfibio.cantidadAnfibios())

    def setZona(self,zona):
        self._zona=zona
