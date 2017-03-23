import random
from unittest import TestCase

from kMeans import KMeans


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

        data3=[1,2,3]
        cluster1, cluster2, cluster3 = self.k.setupClusters(data3)
        self.assertEqual(len(cluster1)+len(cluster2)+len(cluster3), len(data3))
        self.assertTrue(set(cluster1)<set(data3))
        self.assertTrue(set(cluster2)<set(data3))
        self.assertTrue(set(cluster3)<set(data3))
        self.assertNotEqual(cluster3,cluster2)
        self.assertNotEqual(cluster3,cluster1)
        self.assertNotEqual(cluster2,cluster1)
        self.assertItemsEqual(data3,cluster1+cluster2+cluster3)

        data4=[1,2,3,4,6]
        cluster1, cluster2, cluster3 = self.k.setupClusters(data4)
        self.assertEqual(len(cluster1)+len(cluster2)+len(cluster3), len(data4))
        self.assertTrue(set(cluster1)<set(data4))
        self.assertTrue(set(cluster2)<set(data4))
        self.assertTrue(set(cluster3)<set(data4))
        self.assertNotEqual(cluster3,cluster2)
        self.assertNotEqual(cluster3,cluster1)
        self.assertNotEqual(cluster2,cluster1)
        self.assertItemsEqual(data4,cluster1+cluster2+cluster3)


        data5=[1,2,3,4,5,6,7]
        cluster1, cluster2, cluster3 = self.k.setupClusters(data5)
        self.assertEqual(len(cluster1)+len(cluster2)+len(cluster3), len(data5))
        self.assertTrue(set(cluster1)<set(data5))
        self.assertTrue(set(cluster2)<set(data5))
        self.assertTrue(set(cluster3)<set(data5))
        self.assertNotEqual(cluster3,cluster2)
        self.assertNotEqual(cluster3,cluster1)
        self.assertNotEqual(cluster2,cluster1)
        self.assertItemsEqual(data5,cluster1+cluster2+cluster3)

        data6 = random.sample(range(1, 100), 99)
        cluster1, cluster2, cluster3 = self.k.setupClusters(data6)
        self.assertEqual(len(cluster1)+len(cluster2)+len(cluster3), len(data6))
        self.assertTrue(set(cluster1)<set(data6))
        self.assertTrue(set(cluster2)<set(data6))
        self.assertTrue(set(cluster3)<set(data6))
        self.assertNotEqual(cluster3,cluster2)
        self.assertNotEqual(cluster3,cluster1)
        self.assertNotEqual(cluster2,cluster1)
        self.assertItemsEqual(data6,cluster1+cluster2+cluster3)

        pass
    def test_addElementToCluster(self):
        pass
