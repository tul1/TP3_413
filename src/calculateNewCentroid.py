'''
La classe CalculateNewCentroid sert a determiner le nouveau centroides d'un cluster de differentes manieres.
Les methode de la classe sont:
    + average determine le nouveau centroid en calculant une moyenne des valeurs du cluster. 
    + median determine le nouveau centroid en calculant une moyenne des valeurs du cluster. 

On a valide toujours les entrees des fonction.
Si les arguments passes au metodes ne sont pas bon la metode returne None.
Argument attendu: 
cluster=[]
'''
import random
import numpy


FUNCTIONS_NAMES=['averageNewCentroids','medianNewCentroids']

class CalculateNewCentroid:
    def __init__(self, methodName=None):
        if methodName not in FUNCTIONS_NAMES:
            self.methodName = None
        else:
            self.methodName = methodName
        pass

    def evalProcess(self,cluster=None):
        # TODO AGREGAR VALIDACIONES ACA
        if cluster==None: return None

        method = getattr(self,self.methodName)
        return method(cluster)


    def averageNewCentroids(self,cluster=None):
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

    def medianNewCentroids(self, cluster=None):
        if cluster!=None and len(cluster)!=0:
            if isinstance(cluster,(list,int,long,float))==False: return None

            if isinstance(cluster[0]['array'],list)==True:
                maxVal = numpy.zeros(len(cluster[0]['array']))
                minVal = numpy.zeros(len(cluster[0]['array']))
            else:
                maxVal = numpy.zeros(1)
                minVal = numpy.zeros(1)

            for vector in cluster:
                if isinstance(vector['array'],(list,int,long,float))==False: return None
                if isinstance(vector['array'],(list))==True:
                    if all(isinstance(item,(float,int,long)) for item in vector['array'])==False:
                        return None
                val = numpy.array(vector['array'])
                if numpy.linalg.norm(maxVal) <= numpy.linalg.norm(val):
                    maxVal = val
                if numpy.linalg.norm(maxVal) >= numpy.linalg.norm(val):
                    minVal = val
            return ((maxVal+minVal)/2).tolist()
        return None


    def random(self, cluster=None):
        if cluster!=None and len(cluster)!=0:
            if isinstance(cluster,(list,int,long,float))==False: return None
            for vector in cluster:
                if isinstance(vector['array'],(list,int,long,float))==False: return None
                if isinstance(vector['array'],(list))==True:
                    if all(isinstance(item,(float,int,long)) for item in vector['array'])==False:
                        return None
            return random.choice(cluster)['array']
        return None