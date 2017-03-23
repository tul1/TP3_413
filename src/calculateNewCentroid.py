'''
La classe CalculateNewCentroid sert a determiner le nouveau centroides d'un cluster de differentes manieres.
Les metode de la classe sont:
    + average determine le nouveau centroid en calcular une moyenne des valeurs.
    +

On a valide les entrees des fonction.
Si les arguments passes au metodes ne sont pas bon la metode returne None.
Cette fonctions de cette classe peut recevoir listes, tuples ou bien dictionnaires.
'''

class CalculateNewCentroid:
    def __init__(self):
        pass
    def average(self,c):
        if c!=None and len(c)!=0:
            sum = 0.0
            for e in c:
                if isinstance(e, (int, long, float))==False:
                    return None
                sum += e
            return sum/len(c)
        return None