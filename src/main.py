from kMeans import KMeans

FILE_NAME = "irisData.txt"

def readData(fName):
    if fName==None:
        return None
    with open(fName) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    inputData=[]
    for c in content:
        aux = c.split(',')
        d = {'cluster':'', 'array':[]}
        d['cluster'] = aux.pop()
        aux.reverse()
        while len(aux)>0:
            d['array'].append(float(aux.pop()))
        inputData.append(d)
    return inputData

if __name__ == "__main__":

    rawData=readData(FILE_NAME)

    k = KMeans()
    processData = k.setupClustersISIS(rawData)



