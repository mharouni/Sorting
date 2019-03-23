#!/usr/bin/python
import BubbleSort
import RandomArray
import QuickSort
import MergeSort
import SelectionSort
import InsertionSort
import heaps
import time
n = 200
a= RandomArray.Gen(n)
start = time.time()
QuickSort.sort(a, 0, n-1)
end = time.time()
print("QuickSort: "+ str(end - start))
a= RandomArray.Gen(n)
start = time.time()
MergeSort.sort(a)
end = time.time()
print("MergeSort: "+str(end - start))
a= RandomArray.Gen(n)
heaps.Sort(a)
a= RandomArray.Gen(n)
BubbleSort.sort(a)
a= RandomArray.Gen(n)
SelectionSort.sort(a)
a= RandomArray.Gen(n)
InsertionSort.sort(a)
