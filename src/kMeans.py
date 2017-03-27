'''
La classe KMeans applique le critere de selection par clusters.
Les methode de la classe sont:
    + setupClusters clasifie l'information d'entree en 3 clusters. 
'''

from calculateNewCentroid import CalculateNewCentroid
from determinateInitialCentroids import DeterminateInitialCentroids
from mesureDistance import MesureDistance

class KMeans:
    def __init__(self,initialCentroids=None,determineNewCentroids=None,distanceCalcul=None):
        self.determinateInitCentroids = DeterminateInitialCentroids(initialCentroids)
        self.mesureDistance = MesureDistance(distanceCalcul)
        self.calcNewCentroid = CalculateNewCentroid(determineNewCentroids)
        pass

    def setupClusters(self,collection):
        if collection==None or not isinstance(collection,(list,tuple,dict)) or len(collection)<3:
            return None

        self.rawData_ = collection

        oldCentroidCluster1 = oldCentroidCluster2 = oldCentroidCluster3 = None
        newCentroidCluster1 = newCentroidCluster2 = newCentroidCluster3 = None

        newCentroidCluster1, newCentroidCluster2, newCentroidCluster3 = self.determinateInitCentroids.evalProcess(self.rawData_)

        while oldCentroidCluster1 != newCentroidCluster1 \
                or oldCentroidCluster2 != newCentroidCluster2 \
                or oldCentroidCluster3 != newCentroidCluster3:
            self.cluster1_ = []
            self.cluster2_ = []
            self.cluster3_ = []

            oldCentroidCluster1 = newCentroidCluster1
            oldCentroidCluster2 = newCentroidCluster2
            oldCentroidCluster3 = newCentroidCluster3

            for element in self.rawData_:

                d1 = self.mesureDistance.evalProcess(oldCentroidCluster1, element['array'])
                d2 = self.mesureDistance.evalProcess(oldCentroidCluster2, element['array'])
                d3 = self.mesureDistance.evalProcess(oldCentroidCluster3, element['array'])

                if d1 <= d2 and d1 < d3: self.cluster1_.append(element)
                if d2 < d1 and d2 <= d3: self.cluster2_.append(element)
                if d3 <= d1 and d3 < d2: self.cluster3_.append(element)

            newCentroidCluster1 = self.calcNewCentroid.evalProcess(self.cluster1_)
            newCentroidCluster2 = self.calcNewCentroid.evalProcess(self.cluster2_)
            newCentroidCluster3 = self.calcNewCentroid.evalProcess(self.cluster3_)

        return ({'cluster':self.cluster1_,'centroid': newCentroidCluster1},
                {'cluster': self.cluster2_, 'centroid': newCentroidCluster2},
                {'cluster': self.cluster3_, 'centroid': newCentroidCluster3})
