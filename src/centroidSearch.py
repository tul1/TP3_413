from src.calculateNewCentroid import CalculateNewCentroid as c
from src.determinateInitialCentroids import DeterminateInitialCentroids as cs
from src.mesureDistance import MesureDistance as m

def CentroidSearch(array):
    cluster1=[]
    cluster2=[]
    cluster3=[]
    oldCentroid_1 = oldCentroid_2 = oldCentroid_3 = newCentroid_1 = newCentroid_2 = newCentroid_3 = None

    # TODO poner un callback generico
    cs.randomCentroids(array, newCentroid_1, newCentroid_2, newCentroid_3)

    while oldCentroid_1 != newCentroid_1 or oldCentroid_2 != newCentroid_2 or oldCentroid_3 != newCentroid_3:
        cluster1 = []
        cluster2 = []
        cluster3 = []
        oldCentroid_1 = newCentroid_1
        oldCentroid_2 = newCentroid_2
        oldCentroid_3 = newCentroid_3
        for element in array:
            # TODO poner un callback generico
            d1=m.euclidian(oldCentroid_1, element)
            d2=m.euclidian(oldCentroid_2, element)
            d3=m.euclidian(oldCentroid_3, element)
            if d1<d2 and d1<d3: cluster1.append(element)
            if d2<d1 and d2<d3: cluster2.append(element)
            if d3<d1 and d3<d2: cluster3.append(element)
        newCentroid_1 = c.average(cluster1)
        newCentroid_2 = c.average(cluster2)
        newCentroid_3 = c.average(cluster3)
    return cluster1, cluster2, cluster3