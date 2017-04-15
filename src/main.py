from kMeans import KMeans
from utils import plotResults, readData, printTestSummary, printToFile

#CONSTANTS
#combinaisons des tests que le programme va realiser
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
# Nom des fichiers d'entree et sortie du programme
INPUT_FILE_NAME = "irisData.txt"
OUTPUT_FILE_NAME = "resultatsKMeans.txt"

#Function que applique les tests
def applyTest(tst,rawData):
    k = KMeans(tst['centroidDet'], tst['recombMet'], tst['distance'])
    return k.setupClusters(rawData)

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
        resultTest+=printTestSummary(rslt)
        testNum+=1
        plotResults(rslt, tst['centroidDet']+'_'+tst['recombMet']+'_'+tst['distance'])
    printToFile(resultTest)s