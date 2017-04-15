import random
from unittest import TestCase

from src.determinateInitialCentroids import DeterminateInitialCentroids


class TestDeterminateInitialCentroids(TestCase):
    def setUp(self):
        self.d = DeterminateInitialCentroids()
        pass

    def test_randomCentroids(self):
        self.assertIsNone(self.d.randomCentroids(1))
        self.assertIsNone(self.d.randomCentroids('a'))

        a0=[]
        self.assertIsNone(self.d.randomCentroids(a0))
        a1=[1]
        self.assertIsNone(self.d.randomCentroids(a1))
        a2=[1,2]
        self.assertIsNone(self.d.randomCentroids(a2))

        t0=()
        self.assertIsNone(self.d.randomCentroids(t0))
        t1=(1)
        self.assertIsNone(self.d.randomCentroids(t1))
        t2=(1,2)
        self.assertIsNone(self.d.randomCentroids(t2))

        d0={}
        self.assertIsNone(self.d.randomCentroids(d0))
        d1=(1)
        self.assertIsNone(self.d.randomCentroids(d1))
        d2=(1,2)
        self.assertIsNone(self.d.randomCentroids(d2))


        a3=[1,2,3]
        c1,c2,c3 = self.d.randomCentroids(a3)
        self.assertEqual(a3,[1,2,3])
        self.assertIn(c1,a3)
        self.assertIn(c2,a3)
        self.assertIn(c3,a3)
        self.assertNotEqual(c1,c2)
        self.assertNotEqual(c3,c2)

        # t3=(1,2,3)
        # c1,c2,c3 = self.d.randomCentroids(t3)
        # self.assertEqual(t3,(1,2,3))
        # self.assertIn(c1,a3)
        # self.assertIn(c2,a3)
        # self.assertIn(c3,a3)

        # d3={1,2,3}
        # c1,c2,c3 = self.d.randomCentroids(t3)
        # self.assertEqual(t3,{1,2,3})
        # self.assertIn(c1,a3)
        # self.assertIn(c2,a3)
        # self.assertIn(c3,a3)


        a4=random.sample(range(1, 100), 99)
        c1,c2,c3 = self.d.randomCentroids(a4)
        self.assertIn(c1, a4)
        self.assertIn(c2, a4)
        self.assertIn(c3, a4)
        self.assertNotEqual(c1, c2)
        self.assertNotEqual(c3, c2)
        pass

    def test_binSearchCentroids(self):
        pass