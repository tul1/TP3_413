'''
La classe CalculateNewCentroid sert a determiner le nouveau centroides d'un cluster de differentes manieres.
Les metode de la classe sont:
    + average determine le nouveau centroid en calcular une moyenne des valeurs.
    +

On a valide les entrees des fonction.
Si les arguments passes au metodes ne sont pas bon la metode returne None.
Cette fonctions de cette classe peut recevoir listes, tuples ou bien dictionnaires.

TODO generaliser pour calculer des moyennes des vecteurs

'''

import numpy


class CalculateNewCentroid:
    def __init__(self, process=None):
        self.process=process
        pass


    def average(self,cluster=None):
        if cluster!=None and len(cluster)!=0:
            if isinstance(cluster,(list,int,long,float))==False: return None

            if isinstance(cluster[0]['array'],list)==True:
                sum = numpy.zeros(len(cluster[0]['array']))
            else:
                sum = numpy.zeros(1)

            for vector in cluster:
                if isinstance(vector['array'],(list,int,long,float))==False: return None

                if isinstance(vector['array'],(list))==True:
                    if all(isinstance(item,(float,int,long)) for item in vector['array'])==False:
                        return None

                sum += numpy.array(vector['array'])
            return (sum/len(cluster)).tolist()
        return None