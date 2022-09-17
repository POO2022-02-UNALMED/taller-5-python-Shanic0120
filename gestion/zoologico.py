class Zoologico:
    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]

    
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        zona.setZoo(self)

    def cantidadTotalAnimales(self):
        x=0
        for i in self._zonas:
            x=x+i.cantidadAnimales()
        return x
