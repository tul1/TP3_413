'''
La classe DeterminateInitialCentroids sert a determiner 3 centroides des cluster de differentes facons.
Les metode de la classe sont:
    + randomCentroids qui determine aleatoirement les 3 centroides. Il recoit un tableau avec le contenue
        de clusters.
    + pretretedInputDataInitialCentroidsFar qui d'abord tri l'ensemble des elements et puis il choisi comme
        centroides des clusters sur les positions du tableau:  quantiteElementsATraiter/4, quantiteElementsATraiter/2 
        et etquantiteElementsATraiter*3/4.
    + initialCentroidsNextToEachOther determine les trois primiers elements de la liste como les centroides des clusters.

On a valide les entrees des fonction.
Si les arguments passes au methodes ne sont pas bons la methode returne None.
Les trois methodes de traitement de donnees retourne les trois centroides.
'''
import random
import copy

from quicksort import quickSort

FUNCTIONS_NAMES=['randomInitialCentroids','pretretedInputDataInitialCentroidsNear','initialCentroidsNextToEachOther']

class DeterminateInitialCentroids:
    # Le constructeur selectione la methode qui va etre utilisee.
    def __init__(self, methodName=None):
        if methodName not in FUNCTIONS_NAMES:
            self.methodName = None
        else:
            self.methodName = methodName
        pass

    def evalProcess(self, array):
        if self.methodName==None:
            return None
        if array!=None and isinstance(array, (list, tuple, dict)) and len(array)>2:
            if isinstance(array, (tuple, dict)):
                print "no develop yet!"
                return None
        method = getattr(self,self.methodName)
        return method(array)

    def randomInitialCentroids(self, array):
        aux = copy.copy(array)
        centre1=random.choice(aux)
        aux.pop(aux.index(centre1))
        centre2=random.choice(aux)
        aux.pop(aux.index(centre2))
        centre3=random.choice(aux)
        return centre1['array'], centre2['array'], centre3['array']

    def pretretedInputDataInitialCentroidsNear(self,array):
        quickSort(array)
        center1=array[int(len(array)/4)]
        centre2=array[int(len(array)/2)]
        centre3=array[int(len(array)*3/4)]
        return center1['array'], centre2['array'], centre3['array']

    def initialCentroidsNextToEachOther(self, array):
        center1 = array[0]
        centre2 = array[2]
        centre3 = array[3]
        return center1['array'], centre2['array'], centre3['array']