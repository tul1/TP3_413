from unittest import TestCase

from mesureDistance import MesureDistance

class TestMesureDistance(TestCase):
    def setUp(self):
        self.m=MesureDistance()
        pass
    def test_euclidian(self):

        self.assertIsNone(self.m.euclidian('a', 3))
        self.assertIsNone(self.m.euclidian([1,2],1))
        self.assertIsNone(self.m.euclidian(['q',2],1))
        self.assertIsNone(self.m.euclidian({1,2},1))
        self.assertIsNone(self.m.euclidian({'d',2},1))
        self.assertIsNone(self.m.euclidian((1,1),1))
        self.assertIsNone(self.m.euclidian((1,'a'),1))

        self.assertIsNone(self.m.euclidian(2,'b'))
        self.assertIsNone(self.m.euclidian(1,[1,2]))
        self.assertIsNone(self.m.euclidian(1,[1,'a']))
        self.assertIsNone(self.m.euclidian(1,{1,2}))
        self.assertIsNone(self.m.euclidian(1,{1,'a'}))
        self.assertIsNone(self.m.euclidian(1,(1,1)))
        self.assertIsNone(self.m.euclidian(1,(1,'a')))

        self.assertIsNone(self.m.euclidian('a','b'))
        self.assertIsNone(self.m.euclidian([1,2],[1,2]))
        self.assertIsNone(self.m.euclidian([1,'a'],[1,'a']))
        self.assertIsNone(self.m.euclidian({1,2},{1,2}))
        self.assertIsNone(self.m.euclidian({1,'a'},{1,'a'}))
        self.assertIsNone(self.m.euclidian((1,1),(1,1)))
        self.assertIsNone(self.m.euclidian((1,'a'),(1,'a')))

        self.assertEqual(self.m.euclidian(2,1),1)
        self.assertEqual(self.m.euclidian(1,2),1)
        self.assertEqual(self.m.euclidian(0,0),0)

        self.assertEqual(self.m.euclidian(1.7,2.5), 0.8)

        pass

    def test_manhattan(self):
        pass