class CalculateNewCentroid:
    def average(self,c):
        if c!=None:
            sum = 0
            for e in c:
                sum += e
            return sum/len(cluster)
        return None