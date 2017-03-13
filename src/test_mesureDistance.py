from unittest import TestCase

from src import mesureDistance


class TestMesureDistance(TestCase):
    def test_euclidian(self):

        self.assertIsNone(mesureDistance.euclidian(1,'a'))
        self.assertIsNone(mesureDistance.euclidian('s','s'))
        self.assertIsNone(mesureDistance.euclidian('s',3))

        self.assertEqual(mesureDistance.euclidian(1,-1), 2)
        self.assertEqual(mesureDistance.euclidian(1,3), 1)

        pass

    def test_manhatan(self):
        pass