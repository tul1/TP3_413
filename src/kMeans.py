
from calculateNewCentroid import CalculateNewCentroid
from determinateInitialCentroids import DeterminateInitialCentroids
from mesureDistance import MesureDistance

class KMeans:
    def __init__(self):
        self.cs = DeterminateInitialCentroids()

        self.m = MesureDistance()

        self.c = CalculateNewCentroid()

        pass

    # TODO HACER GENERICO LA CANTIDAD DE CLUSTER
    def setupClusters(self,collection):
        if collection==None or not isinstance(collection,(list,tuple,dict)) or len(collection)<3:
            return None

        self.rawData_ = collection

        oldCentroidCluster1 = oldCentroidCluster2 = oldCentroidCluster3 = None
        newCentroidCluster1 = newCentroidCluster2 = newCentroidCluster3 = None

        # TODO poner un callback generico para poder usar distintas
        newCentroidCluster1, newCentroidCluster2, newCentroidCluster3 = self.cs.randomCentroids(self.rawData_)

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
                d1 = self.m.euclidian(oldCentroidCluster1, element['array'])
                d2 = self.m.euclidian(oldCentroidCluster2, element['array'])
                d3 = self.m.euclidian(oldCentroidCluster3, element['array'])

                if d1 <= d2 and d1 < d3: self.cluster1_.append(element)
                if d2 < d1 and d2 <= d3: self.cluster2_.append(element)
                if d3 <= d1 and d3 < d2: self.cluster3_.append(element)

            # TODO poner un callback generico
            newCentroidCluster1 = self.c.average(self.cluster1_)
            newCentroidCluster2 = self.c.average(self.cluster2_)
            newCentroidCluster3 = self.c.average(self.cluster3_)

        return self.cluster1_, self.cluster2_, self.cluster3_, newCentroidCluster1, newCentroidCluster2, newCentroidCluster3
