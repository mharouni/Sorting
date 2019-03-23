#!/usr/bin/python
import time
def heapify(arr=[1,2,3,4,5,6,7,8],n=8,i=8):
	largest = i
	l = 2 * i +1
	r = 2 * i +2
	if l < n and arr[i] < arr[l]:
		largest = l
	if r < n and arr[i] < arr [r]:
		largest = r 
	if largest != i:
		arr[i],arr[largest]= arr[largest],arr[i]
		heapify(arr,n,(i-1//2))
		heapify(arr, n, largest)
	return arr
def Sort(arr):
	start = time.time()
	n = len(arr)  
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)
	end = time.time()
	print("HeapSort: " +str(end - start))
	#return arr
#print(heapSort([1,2,3,4,5,6,7,8]))


