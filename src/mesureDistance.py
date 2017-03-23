
class MesureDistance:
    def __init__(self):
        pass
    def euclidian(self, a, b):
        if a==None or b==None or isinstance(a, (int, long, float))==False or isinstance(b, (int, long, float))==False:
            return None
        return abs(float(a)-float(b))

    def manhattan(self,a,b):
        return float(a)+float(b)


