import random
from unittest import TestCase

from src.kMeans import KMeans


class TestKMeans(TestCase):
    def setUp(self):
        self.k=KMeans()
        pass


    def test_setupClusters(self):

        self.assertIsNone(self.k.setupClusters(None))
        data0=[]
        self.assertIsNone(self.k.setupClusters(data0))
        data1=[1]
        self.assertIsNone(self.k.setupClusters(data1))
        data2=[1,2]
        self.assertIsNone(self.k.setupClusters(data2))

        def testList(name, data):
            cluster1, cluster2, cluster3, c1, c2, c3 = self.k.setupClusters(data)
            print "Test Name: " + name
            print "Input data:"
            print data
            print "Unsorted Clusters and centroid:"
            print str(cluster1) + " .. " + str(c1)
            print str(cluster2) + " .. " + str(c2)
            print str(cluster3) + " .. " + str(c3)
            print "Sorted Clusters and centroid:"
            print str(sorted(cluster1)) + " .. " + str(c1)
            print str(sorted(cluster2)) + " .. " + str(c2)
            print str(sorted(cluster3)) + " .. " + str(c3)

            print "---------------------------------------------------"

            self.assertEqual(len(cluster1) + len(cluster2) + len(cluster3), len(data))
            self.assertTrue(set(cluster1) < set(data))
            self.assertTrue(set(cluster2) < set(data))
            self.assertTrue(set(cluster3) < set(data))
            self.assertNotEqual(cluster3, cluster2)
            self.assertNotEqual(cluster3, cluster1)
            self.assertNotEqual(cluster2, cluster1)
            self.assertItemsEqual(data, cluster1 + cluster2 + cluster3)
            pass

        data3=[1,2,3]
        testList("Sorted list 3 elements",data3)

        data4=[1,2,3,4,5]
        testList("Sorted list 5 elements",data4)

        data5=[1,2,3,4,5,6,7]
        testList("Sorted list 7 elements",data5)

        data6 = random.sample(range(1, 100), 99)
        testList("Unsorted list 100 elements",data6)

        pass


    def test_addElementToCluster(self):
        pass
