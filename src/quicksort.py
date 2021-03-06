'''
Version modifier de l'algorithme quickSort por trier des vecteur de 4 elements.
La function quickSort recoit comme argument une liste de vecteurs.
'''

import numpy.linalg

def quickSort(alist):
    return quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = numpy.linalg.norm(numpy.array((alist[first]['array'])))

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and numpy.linalg.norm(numpy.array((alist[leftmark]['array']))) <= pivotvalue:
            leftmark = leftmark + 1

        while numpy.linalg.norm(numpy.array((alist[rightmark]['array']))) >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark