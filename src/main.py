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
    clusterNum=1
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
        out += '------------------- Cluster'+ str(clusterNum) +' -------------------\n'
        out += 'Centroid: ' + str(cluster['centroid'])+'\n'
        out += 'Versicolor: ' + str(porcenVersicolor)+'\n'
        out += 'Setosa: ' + str(porcenSetosa)+'\n'
        out += 'virginica: ' + str(porcenVirginica)+'\n'
        clusterNum+=1
    return out+'\n\n\n'


def applyTest(tst,rawData):
    k = KMeans(tst['centroidDet'], tst['recombMet'], tst['distance'])
    return k.setupClusters(rawData)

def printToFile(outStr):
    print outStr
    f=open(OUTPUT_FILE_NAME,'w+')
    f.write(outStr)
    f.close()


#CONSTANTES
tests=[
    {'centroidDet': 'initialCentroidsNextToEachOther', 'recombMet': 'averageNewCentroids','distance': 'euclideanDistance'},
    {'centroidDet': 'initialCentroidsNextToEachOther', 'recombMet': 'averageNewCentroids','distance': 'manhattanDistance'},
    {'centroidDet': 'initialCentroidsNextToEachOther', 'recombMet': 'medianNewCentroids','distance': 'euclideanDistance'},
    {'centroidDet': 'initialCentroidsNextToEachOther', 'recombMet': 'medianNewCentroids','distance': 'manhattanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'averageNewCentroids', 'distance':'euclideanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'averageNewCentroids', 'distance': 'manhattanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'medianNewCentroids','distance': 'euclideanDistance'},
    {'centroidDet': 'pretretedInputDataInitialCentroidsNear', 'recombMet': 'medianNewCentroids', 'distance': 'manhattanDistance'},
    {'centroidDet': 'randomInitialCentroids', 'recombMet': 'averageNewCentroids', 'distance': 'euclideanDistance'},
    {'centroidDet': 'randomInitialCentroids', 'recombMet': 'averageNewCentroids', 'distance': 'manhattanDistance'},
    {'centroidDet': 'randomInitialCentroids', 'recombMet': 'medianNewCentroids', 'distance': 'euclideanDistance'},
    {'centroidDet': 'randomInitialCentroids', 'recombMet': 'medianNewCentroids', 'distance': 'manhattanDistance'}
]
INPUT_FILE_NAME = "irisData.txt"
OUTPUT_FILE_NAME = "resultatsKMeans.txt"


if __name__ == "__main__":
    data=readData(INPUT_FILE_NAME)
    resultTest=''
    testNum=1
    for tst in tests:
        resultTest += '------------------------------------ Test N '+str(testNum)+' ------------------------------------\n'
        resultTest+='Centroid determination method: ' + tst['centroidDet'] +'\n'
        resultTest+='New centroid determination method: ' + tst['recombMet'] +'\n'
        resultTest += 'Distance method: ' + tst['distance'] + '\n'
        rslt, iterations=applyTest(tst, data)
        resultTest += 'Quantite iterations: ' + str(iterations) + '\n'
        resultTest+=getTestSummary(rslt)
        testNum+=1
    printToFile(resultTest)

    exp = {'centroidDet': 'randomInitialCentroids', 'recombMet': 'averageNewCentroids', 'distance': 'euclideanDistance'}
    rslt, iterations = applyTest(exp, data)
    listAux=[]
    #agregar todos los elementos
    listAux.append()
    listAux.append(rslt[1]['cluster'])
    listAux.append(rslt[2]['cluster'])
    print listAux


[[{'clusterName': 'Iris-virginica', 'array': [6.1, 2.6, 5.6, 1.4]}, {'clusterName': 'Iris-virginica', 'array': [6.4, 2.7, 5.3, 1.9]}, {'clusterName': 'Iris-versicolor', 'array': [6.7, 3.0, 5.0, 1.7]}, {'clusterName': 'Iris-virginica', 'array': [6.5, 3.0, 5.2, 2.0]}, {'clusterName': 'Iris-virginica', 'array': [6.5, 3.2, 5.1, 2.0]}, {'clusterName': 'Iris-virginica', 'array': [6.3, 2.9, 5.6, 1.8]}, {'clusterName': 'Iris-versicolor', 'array': [7.0, 3.2, 4.7, 1.4]}, {'clusterName': 'Iris-versicolor', 'array': [6.9, 3.1, 4.9, 1.5]}, {'clusterName': 'Iris-virginica', 'array': [6.4, 3.1, 5.5, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [6.2, 3.4, 5.4, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [6.4, 2.8, 5.6, 2.1]}, {'clusterName': 'Iris-virginica', 'array': [6.4, 3.2, 5.3, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [6.5, 3.0, 5.5, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [6.4, 2.8, 5.6, 2.2]}, {'clusterName': 'Iris-virginica', 'array': [6.7, 3.0, 5.2, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [6.7, 2.5, 5.8, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [6.3, 3.4, 5.6, 2.4]}, {'clusterName': 'Iris-virginica', 'array': [6.9, 3.1, 5.1, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [6.5, 3.0, 5.8, 2.2]}, {'clusterName': 'Iris-virginica', 'array': [6.8, 3.0, 5.5, 2.1]}, {'clusterName': 'Iris-virginica', 'array': [6.9, 3.1, 5.4, 2.1]}, {'clusterName': 'Iris-virginica', 'array': [6.7, 3.1, 5.6, 2.4]}, {'clusterName': 'Iris-virginica', 'array': [6.7, 3.3, 5.7, 2.1]}, {'clusterName': 'Iris-virginica', 'array': [6.3, 3.3, 6.0, 2.5]}, {'clusterName': 'Iris-virginica', 'array': [6.7, 3.3, 5.7, 2.5]}, {'clusterName': 'Iris-virginica', 'array': [6.9, 3.2, 5.7, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [6.8, 3.2, 5.9, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [7.2, 3.0, 5.8, 1.6]}, {'clusterName': 'Iris-virginica', 'array': [7.1, 3.0, 5.9, 2.1]}, {'clusterName': 'Iris-virginica', 'array': [7.2, 3.2, 6.0, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [7.4, 2.8, 6.1, 1.9]}, {'clusterName': 'Iris-virginica', 'array': [7.3, 2.9, 6.3, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [7.2, 3.6, 6.1, 2.5]}, {'clusterName': 'Iris-virginica', 'array': [7.7, 3.0, 6.1, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [7.6, 3.0, 6.6, 2.1]}, {'clusterName': 'Iris-virginica', 'array': [7.7, 2.8, 6.7, 2.0]}, {'clusterName': 'Iris-virginica', 'array': [7.7, 2.6, 6.9, 2.3]}, {'clusterName': 'Iris-virginica', 'array': [7.9, 3.8, 6.4, 2.0]}, {'clusterName': 'Iris-virginica', 'array': [7.7, 3.8, 6.7, 2.2]}], [{'clusterName': 'Iris-setosa', 'array': [4.5, 2.3, 1.3, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [4.3, 3.0, 1.1, 0.1]}, {'clusterName': 'Iris-setosa', 'array': [4.4, 2.9, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.4, 3.0, 1.3, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.4, 3.2, 1.3, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.6, 3.1, 1.5, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.6, 3.2, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.8, 3.0, 1.4, 0.1]}, {'clusterName': 'Iris-setosa', 'array': [4.7, 3.2, 1.3, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.8, 3.0, 1.4, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [4.6, 3.4, 1.4, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [4.7, 3.2, 1.6, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.9, 3.0, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.6, 3.6, 1.0, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.8, 3.1, 1.6, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.9, 3.1, 1.5, 0.1]}, {'clusterName': 'Iris-setosa', 'array': [4.9, 3.1, 1.5, 0.1]}, {'clusterName': 'Iris-setosa', 'array': [4.9, 3.1, 1.5, 0.1]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.0, 1.6, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.2, 1.2, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.8, 3.4, 1.6, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.3, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [4.8, 3.4, 1.9, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.4, 1.5, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.5, 1.3, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.4, 1.6, 0.4]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.4, 1.5, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.6, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.3, 1.7, 0.5]}, {'clusterName': 'Iris-setosa', 'array': [5.0, 3.5, 1.6, 0.6]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.5, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.5, 1.4, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [5.2, 3.4, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.2, 3.5, 1.5, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.7, 1.5, 0.4]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.8, 1.5, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.8, 1.6, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.4, 3.4, 1.5, 0.4]}, {'clusterName': 'Iris-setosa', 'array': [5.4, 3.4, 1.7, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.3, 3.7, 1.5, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.1, 3.8, 1.9, 0.4]}, {'clusterName': 'Iris-setosa', 'array': [5.5, 3.5, 1.3, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.4, 3.7, 1.5, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.2, 4.1, 1.5, 0.1]}, {'clusterName': 'Iris-setosa', 'array': [5.4, 3.9, 1.3, 0.4]}, {'clusterName': 'Iris-setosa', 'array': [5.4, 3.9, 1.7, 0.4]}, {'clusterName': 'Iris-setosa', 'array': [5.5, 4.2, 1.4, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.7, 3.8, 1.7, 0.3]}, {'clusterName': 'Iris-setosa', 'array': [5.8, 4.0, 1.2, 0.2]}, {'clusterName': 'Iris-setosa', 'array': [5.7, 4.4, 1.5, 0.4]}], [{'clusterName': 'Iris-versicolor', 'array': [4.9, 2.4, 3.3, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.0, 2.3, 3.3, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.0, 2.0, 3.5, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.1, 2.5, 3.0, 1.1]}, {'clusterName': 'Iris-versicolor', 'array': [5.5, 2.4, 3.7, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.2, 2.7, 3.9, 1.4]}, {'clusterName': 'Iris-versicolor', 'array': [5.5, 2.4, 3.8, 1.1]}, {'clusterName': 'Iris-versicolor', 'array': [5.7, 2.6, 3.5, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.5, 2.3, 4.0, 1.3]}, {'clusterName': 'Iris-virginica', 'array': [4.9, 2.5, 4.5, 1.7]}, {'clusterName': 'Iris-versicolor', 'array': [5.6, 2.5, 3.9, 1.1]}, {'clusterName': 'Iris-versicolor', 'array': [5.5, 2.5, 4.0, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.6, 2.9, 3.6, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.8, 2.7, 3.9, 1.2]}, {'clusterName': 'Iris-versicolor', 'array': [5.5, 2.6, 4.4, 1.2]}, {'clusterName': 'Iris-versicolor', 'array': [5.8, 2.6, 4.0, 1.2]}, {'clusterName': 'Iris-versicolor', 'array': [6.0, 2.2, 4.0, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.6, 2.7, 4.2, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.8, 2.7, 4.1, 1.0]}, {'clusterName': 'Iris-versicolor', 'array': [5.7, 2.8, 4.1, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.6, 3.0, 4.1, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.7, 2.9, 4.2, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.7, 3.0, 4.2, 1.2]}, {'clusterName': 'Iris-versicolor', 'array': [5.4, 3.0, 4.5, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [5.7, 2.8, 4.5, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [6.1, 2.8, 4.0, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [5.6, 3.0, 4.5, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [5.9, 3.0, 4.2, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.2, 2.2, 4.5, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.3, 2.3, 4.4, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [6.0, 2.9, 4.5, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.2, 2.9, 4.3, 1.3]}, {'clusterName': 'Iris-virginica', 'array': [5.6, 2.8, 4.9, 2.0]}, {'clusterName': 'Iris-virginica', 'array': [5.7, 2.5, 5.0, 2.0]}, {'clusterName': 'Iris-virginica', 'array': [6.0, 2.2, 5.0, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.1, 2.8, 4.7, 1.2]}, {'clusterName': 'Iris-versicolor', 'array': [6.1, 3.0, 4.6, 1.4]}, {'clusterName': 'Iris-versicolor', 'array': [6.4, 2.9, 4.3, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [6.1, 2.9, 4.7, 1.4]}, {'clusterName': 'Iris-versicolor', 'array': [6.0, 3.4, 4.5, 1.6]}, {'clusterName': 'Iris-virginica', 'array': [5.8, 2.7, 5.1, 1.9]}, {'clusterName': 'Iris-virginica', 'array': [5.8, 2.7, 5.1, 1.9]}, {'clusterName': 'Iris-virginica', 'array': [6.0, 3.0, 4.8, 1.8]}, {'clusterName': 'Iris-versicolor', 'array': [5.9, 3.2, 4.8, 1.8]}, {'clusterName': 'Iris-versicolor', 'array': [6.0, 2.7, 5.1, 1.6]}, {'clusterName': 'Iris-versicolor', 'array': [6.3, 2.5, 4.9, 1.5]}, {'clusterName': 'Iris-virginica', 'array': [6.2, 2.8, 4.8, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [5.9, 3.0, 5.1, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [5.8, 2.8, 5.1, 2.4]}, {'clusterName': 'Iris-virginica', 'array': [6.1, 3.0, 4.9, 1.8]}, {'clusterName': 'Iris-versicolor', 'array': [6.5, 2.8, 4.6, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.4, 3.2, 4.5, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.6, 3.0, 4.4, 1.4]}, {'clusterName': 'Iris-virginica', 'array': [6.3, 2.7, 4.9, 1.8]}, {'clusterName': 'Iris-virginica', 'array': [6.3, 2.5, 5.0, 1.9]}, {'clusterName': 'Iris-versicolor', 'array': [6.6, 2.9, 4.6, 1.3]}, {'clusterName': 'Iris-versicolor', 'array': [6.3, 3.3, 4.7, 1.6]}, {'clusterName': 'Iris-virginica', 'array': [6.3, 2.8, 5.1, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.7, 3.1, 4.4, 1.4]}, {'clusterName': 'Iris-versicolor', 'array': [6.7, 3.1, 4.7, 1.5]}, {'clusterName': 'Iris-versicolor', 'array': [6.8, 2.8, 4.8, 1.4]}]]
