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
        print 'Centroid: ' + str(centroidCluster1)
        print 'Versicolor: ' + str(porcenVersicolor)
        print 'Setosa: ' + str(porcenSetosa)
        print 'virginica: ' + str(porcenVirginica)


if __name__ == "__main__":
    FILE_NAME = "irisData.txt"

    rawData=readData(FILE_NAME)

    k = KMeans()
    cluster1, cluster2, cluster3, centroidCluster1, centroidCluster2, centroidCluster3 = k.setupClusters(rawData)

    clusters = ({"cluster":cluster1, "centroid":centroidCluster1},
              {"cluster":cluster2, "centroid":centroidCluster2},
              {"cluster": cluster3, "centroid": centroidCluster3})

    printResults(clusters)