'''
La classe CalculateNewCentroid a des differente metodes parmi lesqueles ils sont:
    + Average: qui calcule en faisant un
    + ...

On a valide les entrees des fonction.
Si l'argument n'est pas bon la fonction returne None
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