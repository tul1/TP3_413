from unittest import TestCase

from src.centroidSearch import CentroidSearch


class TestCentroidSearch(TestCase):
    def checkCentroides(self,val1,val2):
        pass

    def test_CentroidSearch(self):

        correctValues={'max':5,'min':0,'mid':3}

        increasingArray = range(0, 5)
        self.assertDictEqual(CentroidSearch(increasingArray),correctValues)

        decreasingArray = range(5, 0, -1)
        self.assertDictEqual(CentroidSearch(decreasingArray),correctValues)

        randomArray = [2,1,4,3,5]
        self.assertDictEqual(CentroidSearch(randomArray),correctValues)

        pass
