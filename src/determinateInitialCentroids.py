'''
La classe DeterminateInitialCentroids sert a determiner 3 centroides des cluster de differentes facons.
Les metode de la classe sont:
    + randomCentroids qui determine aleatoirement les 3 centroides. Il recoit un tableau avec le contenue
        de clusters



On a valide les entrees des fonction.
Si les arguments passes au metodes ne sont pas bon la metode returne None.
TODO developper une solution pour les tuples et les dictionnaires
'''

import random
import copy


class DeterminateInitialCentroids:
    def randomCentroids(self, array):
        if array!=None and isinstance(array, (list, tuple, dict)) and len(array)>2:
            if isinstance(array, (tuple, dict)):
                print "no develop yet!"
                return None
            aux = copy.copy(array)
            centre1=random.choice(aux)
            aux.pop(aux.index(centre1))
            centre2=random.choice(aux)
            aux.pop(aux.index(centre2))
            centre3=random.choice(aux)
            return centre1['array'], centre2['array'], centre3['array']
        return None

    def binSearchCentroids(self,array):
        aux=array
        # TODO
        pass
