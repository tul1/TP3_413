'''
La classe MesureDistance sert a mesurer la distance entre 2 elements du cluster.
Les metode de la classe sont:
    + euclideanDistance calcule la distance entre 2 point en effectuant le calcul euclidien
    + manhattanDistance calcule la distance entre 2 point en effectuant le calcul de manhattan
    
On a valide les entrees des fonction.
Si les arguments passes au methodes ne sont pas bon la methode returne None.
'''
import numpy.linalg

FUNCTIONS_NAMES=['euclideanDistance','manhattanDistance']

class MesureDistance:
    def __init__(self,methodName=None):
        if methodName not in FUNCTIONS_NAMES:
            self.methodName = None
        else:
            self.methodName = methodName
        pass

    def evalProcess(self,a,b):
        # validations
        if a==None or b==None or isinstance(a, (list,int,long,float))==False \
                or isinstance(b, (list,int,long,float))==False:
            return None
        if isinstance(a, (list))==True or isinstance(b, (list))==True:
            if isinstance(a, (list))==False or isinstance(b, (list))==False or len(a)!=len(b):
                return None
            if all(isinstance(item, (float,int,long)) for item in a)==False \
                    or all(isinstance(item, (float,int,long)) for item in b)==False:
                return None
        # Select method
        method = getattr(self,self.methodName)
        return method(a,b)

    def euclideanDistance(self, a, b):
        a=numpy.array(a)
        b=numpy.array(b)
        return numpy.linalg.norm(a-b)

    def manhattanDistance(self,a,b):
        a=numpy.array(a)
        b=numpy.array(b)
        return numpy.sum(numpy.abs(a-b))