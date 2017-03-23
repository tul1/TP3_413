from unittest import TestCase

from calculateNewCentroid import CalculateNewCentroid


class TestCalculateNewCentroid(TestCase):
    def setUp(self):
        self.c=CalculateNewCentroid()
        pass
    def test_average(self):

        self.assertIsNone(self.c.average('w'))
        self.assertIsNone(self.c.average('2'))

        risingCountArray0 = []
        self.assertIsNone(self.c.average(risingCountArray0))

        risingCountArray1 = [1, 1, 1, 1]
        self.assertEqual(self.c.average(risingCountArray1),1)

        risingCountArray2=[1,2,3,4]
        self.assertEqual(self.c.average(risingCountArray2),2.5)

        risingCountArray3=['1','2','3','4']
        self.assertIsNone(self.c.average(risingCountArray3))

        risingCountTupple0 = ()
        self.assertIsNone(self.c.average(risingCountTupple0))

        risingCountTupple1 = (1,2,3,4)
        self.assertEqual(self.c.average(risingCountTupple1),2.5)

        risingCountTupple2 = (2,2,3,'2')
        self.assertIsNone(self.c.average(risingCountTupple2),2.5)

        pass