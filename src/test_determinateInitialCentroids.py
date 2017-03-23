from unittest import TestCase

from determinateInitialCentroids import DeterminateInitialCentroids


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
        t1=(1,2)
        self.assertIsNone(self.d.randomCentroids(t2))

        l0={}
        self.assertIsNone(self.d.randomCentroids(l0))
        l1=(1)
        self.assertIsNone(self.d.randomCentroids(l1))
        l1=(1,2)
        self.assertIsNone(self.d.randomCentroids(l2))

        a3=[1,2,3]
        c1,c2,c3 = self.d.randomCentroids(a3)
        self.assertEqual(a3,[1,2,3])
        self.assertIn(c1,a3)
        self.assertIn(c2,a3)
        self.assertIn(c3,a3)

        t3=(1,2,3)
        c1,c2,c3 = self.d.randomCentroids(t3)
        self.assertEqual(t3,(1,2,3))
        self.assertIn(c1,a3)
        self.assertIn(c2,a3)
        self.assertIn(c3,a3)

        l3={1,2,3}
        c1,c2,c3 = self.d.randomCentroids(l3)
        self.assertEqual(l3,(1,2,3))
        self.assertIn(c1,a3)
        self.assertIn(c2,a3)
        self.assertIn(c3,a3)


        # TODO TEST random array, list and tupple

        pass

    def test_binSearchCentroids(self):
        pass