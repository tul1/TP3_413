import random

class DeterminateInitialCentroids:
    def randomCentroids(self,array):
        if array!=None:
            # TODO verificar si genera copias o pasa referencias, no quiero modificar el arreglo que paso por argumento
            aux = array
            c1=random.choice(aux)
            aux.pop(c1)
            c2=random.choice(aux)
            aux.pop(c2)
            c3=random.choice(aux)
            return c1, c2, c3
        return None

    def binSearchCentroids(self,array):
        aux=array
        pass