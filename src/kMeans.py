'''
La classe KMeans applique le critere de selection par clusters.
Les methode de la classe sont:
    + setupClusters clasifie l'information d'entree en 3 clusters Le retour de la function 
        renvoie les clusters separees et la cantite d'iteration qu'il a prix pour traiter les donnees.
'''

from calculateNewCentroid import CalculateNewCentroid
from determinateInitialCentroids import DeterminateInitialCentroids
from mesureDistance import MesureDistance

class KMeans:
    # Le constructeur determine les parametres de l'algorithme que va etre aplique
    # Les methodes de calcul de la distance entre elements, la determination initial
    #des centroids et le calcule des nouveau centroides dedans des clusters.
    def __init__(self,initialCentroids=None,determineNewCentroids=None,distanceCalcul=None):
        self.determinateInitCentroids = DeterminateInitialCentroids(initialCentroids)
        self.mesureDistance = MesureDistance(distanceCalcul)
        self.calcNewCentroid = CalculateNewCentroid(determineNewCentroids)
        pass

    # La methode setupCluster est le coeur du programme elle aplique l'algorithme de K-Mean a une collection de donnees numeriques.
    # Cette function retournera une tuple aver des dictionnaires ayant les elements: centroid et les element du cluster.
    # Argument attendu: Une list de dictionnaires portant les element 'clusterName' et 'array'.
    # L'element 'clusterName' est le nom du cluster ou la donnee traitee apartien et 'array' c'est une liste de 4 elements qui sera
    #clasifier para ce programme.
    def setupClusters(self,collection):
        if collection==None or not isinstance(collection,(list,tuple,dict)) or len(collection)<3:
            return None

        self.iterations_ = 0
        self.rawData_ = collection

        oldCentroidCluster1 = oldCentroidCluster2 = oldCentroidCluster3 = None
        newCentroidCluster1 = newCentroidCluster2 = newCentroidCluster3 = None

        #D'abord on etablit les position initial des centroides.
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
                #On calcule les distances de toutes les elements avec les trois centroides des clusters.
                d1 = self.mesureDistance.evalProcess(oldCentroidCluster1, element['array'])
                d2 = self.mesureDistance.evalProcess(oldCentroidCluster2, element['array'])
                d3 = self.mesureDistance.evalProcess(oldCentroidCluster3, element['array'])

                #On range les elements dans les clusters avec le centroid le plus proche
                if d1 <= d2 and d1 < d3: self.cluster1_.append(element)
                if d2 < d1 and d2 <= d3: self.cluster2_.append(element)
                if d3 <= d1 and d3 < d2: self.cluster3_.append(element)

                self.iterations_ += 1

            #On recalcule les centroides au sein de chaque cluster
            newCentroidCluster1 = self.calcNewCentroid.evalProcess(self.cluster1_)
            newCentroidCluster2 = self.calcNewCentroid.evalProcess(self.cluster2_)
            newCentroidCluster3 = self.calcNewCentroid.evalProcess(self.cluster3_)

            # On ajoute N iteration car pour calculer les nouveaux centroides il faut N iterations.
            #Etant N la quantite d'elements a traiter.
            self.iterations_ += len(self.rawData_)


        return ({'cluster': self.cluster1_,'centroid': newCentroidCluster1},
                {'cluster': self.cluster2_, 'centroid': newCentroidCluster2},
                {'cluster': self.cluster3_, 'centroid': newCentroidCluster3}), self.iterations_
