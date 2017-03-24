import numpy.linalg

class MesureDistance:
    def __init__(self):
        pass
    def euclidian(self, a, b):
        if a==None or b==None or isinstance(a, (list,int,long,float))==False \
                or isinstance(b, (list,int,long,float))==False:
            return None

        if isinstance(a, (list))==True or isinstance(b, (list))==True:
            if isinstance(a, (list))==False or isinstance(b, (list))==False or len(a)!=len(b):
                return None
            if all(isinstance(item, (float,int,long)) for item in a)==False \
                    or all(isinstance(item, (float,int,long)) for item in b)==False:
                return None

        a=numpy.array(a)
        b=numpy.array(b)
        return numpy.linalg.norm(a-b)


    def manhattan(self,a,b):
        return float(a)+float(b)


