from unittest import TestCase

from src.quicksort import quickSort


class TestQuickSort(TestCase):
    def test_quickSort(self):
        array=[
            {'clusterName': 'Iris-setosa', 'array': [5, 5, 5, 5]},
            {'clusterName': 'Iris-setosa', 'array': [0, 0, 0, 0]},
            {'clusterName': 'Iris-virginica', 'array': [10, 10, 10, 10]},
            {'clusterName': 'Iris-versicolor', 'array': [1, 2.5, 1.4, 0.2]}
        ]
        spectedArray=[
            {'clusterName': 'Iris-setosa', 'array': [0, 0, 0, 0]},
            {'clusterName': 'Iris-versicolor', 'array': [1, 2.5, 1.4, 0.2]},
            {'clusterName': 'Iris-setosa', 'array': [5, 5, 5, 5]},
            {'clusterName': 'Iris-virginica', 'array': [10, 10, 10, 10]}
        ]
        quickSort(array)
        self.assertListEqual(array,spectedArray)

        pass