import copy
from calculateNewCentroid import CalculateNewCentroid
from determinateInitialCentroids import DeterminateInitialCentroids
from mesureDistance import MesureDistance

class KMeans:
    def __init__(self):
        pass

    def setupClusters(self,collection):
        if collection==None or not isinstance(collection,(list,tuple,dict)) or len(collection)<3:
            return None

        self.rawData_ = collection

        oldCentroidCluster1 = oldCentroidCluster2 = oldCentroidCluster3 = None
        newCentroidCluster1 = newCentroidCluster2 = newCentroidCluster3 = None

        cs = DeterminateInitialCentroids()
        m = MesureDistance()
        c = CalculateNewCentroid()

        # TODO poner un callback generico
        newCentroidCluster1, newCentroidCluster2, newCentroidCluster3 = cs.randomCentroids(self.rawData_)

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
                # TODO poner un callback generico

                d1 = m.euclidian(oldCentroidCluster1, element)
                d2 = m.euclidian(oldCentroidCluster2, element)
                d3 = m.euclidian(oldCentroidCluster3, element)

                if d1 < d2 and d1 <= d3:
                    self.cluster1_.append(element)
                if d2 <= d1 and d2 < d3:
                    self.cluster2_.append(element)
                if d3 < d1 and d3 <= d2:
                    self.cluster3_.append(element)

            newCentroidCluster1 = c.average(self.cluster1_)
            newCentroidCluster2 = c.average(self.cluster2_)
            newCentroidCluster3 = c.average(self.cluster3_)
        return self.cluster1_, self.cluster2_, self.cluster3_

    def addElementToCluster(self,val):
        pass