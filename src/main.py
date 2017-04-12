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

def getTestSummary(clusters):
    inputDataSize = sum(len(c['cluster']) for c in clusters)
    out=''
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
        out += '------------------- Results -------------------\n'
        out += 'Centroid: ' + str(cluster['centroid'])+'\n'
        out += 'Versicolor: ' + str(porcenVersicolor)+'\n'
        out += 'Setosa: ' + str(porcenSetosa)+'\n'
        out += 'virginica: ' + str(porcenVirginica)+'\n'
    return out


def applyTest(tst,rawData):
    k = KMeans(tst['centroidDet'], tst['recombMet'], tst['distance'])
    return k.setupClusters(rawData)

#CONSTANTES
tests=[
    {'centroidDet':'pretretedInputDataInitialCentroidsFar', 'recombMet':'averageNewCentroids', 'distance':'euclideanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsFar', 'recombMet': 'averageNewCentroids', 'distance': 'manhattanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsFar', 'recombMet': 'medianNewCentroids','distance': 'euclideanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsFar', 'recombMet': 'medianNewCentroids', 'distance': 'manhattanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'averageNewCentroids','distance': 'euclideanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'averageNewCentroids','distance': 'manhattanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'medianNewCentroids','distance': 'euclideanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'medianNewCentroids', 'distance': 'manhattanDistance'},
    {'centroidDet': 'randomInitialCentroids', 'recombMet': 'averageNewCentroids', 'distance': 'euclideanDistance'}
]
INPUT_FILE_NAME = "irisData.txt"
OUTPUT_FILE_NAME = "resultatsKMeans.txt"

def printToFile(outStr):
    print outStr
    f=open(OUTPUT_FILE_NAME,'w+')
    f.write(outStr)
    f.close()


if __name__ == "__main__":
    data=readData(INPUT_FILE_NAME)
    resultTest=''
    for tst in tests:
        resultTest+=getTestSummary(applyTest(tst,data))
    printToFile(resultTest)