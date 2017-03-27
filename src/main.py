from kMeans import KMeans

def readData(fName):
    if fName==None: return None

    with open(fName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    inputData=[]
    for c in content:
        aux = c.split(',')
        d = {'clusterName':'', 'array':[]}
        d['clusterName'] = aux.pop()
        aux.reverse()
        while len(aux)>0:
            d['array'].append(float(aux.pop()))
        inputData.append(d)
    return inputData

def printResults(clusters):
    inputDataSize = len(rawData)
    for cluster in clusters:
        versicolor = setosa = virginica = 0
        for clusterElement in cluster['cluster']:
            # print clusterElement
            if clusterElement['clusterName']=='Iris-versicolor': versicolor += 1
            if clusterElement['clusterName']=='Iris-setosa': setosa += 1
            if clusterElement['clusterName'] == 'Iris-virginica': virginica += 1
        porcenVersicolor=(100*versicolor/inputDataSize)
        porcenSetosa=(100*setosa/inputDataSize)
        porcenVirginica=(100*virginica/inputDataSize)
        print "------------------- Results -------------------"
        print 'Centroid: ' + str(cluster['centroid'])
        print 'Versicolor: ' + str(porcenVersicolor)
        print 'Setosa: ' + str(porcenSetosa)
        print 'virginica: ' + str(porcenVirginica)




if __name__ == "__main__":
    FILE_NAME = "irisData.txt"

    rawData=readData(FILE_NAME)

    def pretretedInputDataInitialCentroidsFar_averageNewCentroids_euclideanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsFar', 'averageNewCentroids', 'euclideanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def pretretedInputDataInitialCentroidsFar_averageNewCentroids_manhattanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsFar', 'averageNewCentroids', 'manhattanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def pretretedInputDataInitialCentroidsFar_medianNewCentroids_euclideanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsFar', 'medianNewCentroids', 'euclideanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def pretretedInputDataInitialCentroidsFar_medianNewCentroids_manhattanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsFar', 'medianNewCentroids', 'manhattanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def pretretedInputDataInitialCentroidsNear_averageNewCentroids_euclideanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsNear', 'averageNewCentroids', 'euclideanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)


    def pretretedInputDataInitialCentroidsNear_averageNewCentroids_manhattanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsNear', 'averageNewCentroids', 'manhattanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def pretretedInputDataInitialCentroidsNear_medianNewCentroids_euclideanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsNear', 'medianNewCentroids', 'euclideanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def pretretedInputDataInitialCentroidsNear_medianNewCentroids_manhattanDistance():
        k = KMeans('pretretedInputDataInitialCentroidsNear', 'medianNewCentroids', 'manhattanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)


    def randomInitialCentroids_averageNewCentroids_euclideanDistance():
        k = KMeans('randomInitialCentroids', 'averageNewCentroids', 'euclideanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)

    def randomInitialCentroids_averageNewCentroids_euclideanDistance():
        k = KMeans('randomInitialCentroids', 'averageNewCentroids', 'euclideanDistance')
        clusters = k.setupClusters(rawData)
        # TODO MANDAR A UN ARCHIVO
        printResults(clusters)


    randomInitialCentroids_averageNewCentroids_euclideanDistance()
    # pretretedInputDataInitialCentroidsNear_averageNewCentroids_euclideanDistance()
