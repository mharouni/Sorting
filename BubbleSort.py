#!/usr/bin/python
import time
def sort(Arr=[10,1,2,4,5,7,4]):
	start = time.time()
	n= len(Arr)-1
	c=0
	for i in range (n,0,-1):
		for j in range(0,i):
			if Arr[j] > Arr[j+1]:
				Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
	end = time.time()
	print("BubbleSort: "+str(end - start))
	return Arr
		
print(sort([10,9,8,7,6,5,4,3,2,1,-1,-2,-3,-4]))

