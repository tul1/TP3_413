import matplotlib.pyplot as plt

def plotResults(clusters,name):
    flowers={'petals':[],'sepals':[]}
    for c in clusters:
        petals = {'x': [], 'y': []}
        sepals = {'x': [], 'y': []}
        for a in c['cluster']:
            petals['x'].append(a['array'][0])
            petals['y'].append(a['array'][1])
            sepals['x'].append(a['array'][2])
            sepals['y'].append(a['array'][3])
        flowers['petals'].append(petals)
        flowers['sepals'].append(sepals)
    colors=['r','g','b']

    fig = plt.figure(figsize=(15, 10))
    j = 0

    for element in flowers:
        i=0
        algParams=name.split('_')
        plt.title('Determination inicial centroides:  ' + algParams[0] + '\nDetermination des nouveaux centroides:  ' + algParams[1] + '\nDistance:  ' + algParams[2] + '\n')
        plt.subplot(211+j)
        j+=1
        for vector in flowers[element]:
            plt.plot(vector['x'], vector['y'], colors[i]+'o')
            i+=1
        plt.ylabel(element+' width')
        plt.xlabel(element+' length')
    plt.savefig('./graphs/'+name+'_'+element+'.png')
    plt.close(fig)
    pass

def printTestSummary(clusters):
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

def printToFile(outStr):
    f=open(OUTPUT_FILE_NAME,'w+')
    f.write(outStr)
    f.close()