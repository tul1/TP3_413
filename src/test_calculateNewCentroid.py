from unittest import TestCase

import numpy

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

        onesArray1 = [1, 1, 1, 1]
        self.assertEqual(self.c.average(onesArray1), numpy.array([1.0]))

        risingCountArray2=[1,2,3,4]
        self.assertEqual(self.c.average(risingCountArray2),[2.5])

        risingCountArray3=['1','2','3','4']
        self.assertIsNone(self.c.average(risingCountArray3))

        risingCountTupple0 = ()
        self.assertIsNone(self.c.average(risingCountTupple0))

        # TODO AGREGAR UNA VALIDACION PARA TUPLAS
        # risingCountTupple1 = (1,2,3,4)
        # self.assertEqual(self.c.average(risingCountTupple1),[2.5])

        risingCountTupple2 = (2,2,3,'2')
        self.assertIsNone(self.c.average(risingCountTupple2))

        onesVectorArray1 = [[1,1], [1,1], [1,1], [1,1]]
        self.assertEqual( self.c.average(onesVectorArray1),[1.0,1.0])

        onesVectorArray1 = [[1,1,1], [1,1,1], [1,1,1], [1,1,1]]
        self.assertEqual( self.c.average(onesVectorArray1),[1.,1.,1.])

        onesVectorArray1 = [[-1,-1], [-1,1], [1,-1],[1,1]]
        self.assertEqual( self.c.average(onesVectorArray1),[0.,0.])

        onesVectorArray1 = [[-1,-1], [-1,1], [1,-1],[1,1]]
        self.assertEqual( self.c.average(onesVectorArray1),[0.,0.])

        pass