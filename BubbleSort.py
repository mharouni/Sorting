#!/usr/bin/python
import time
def sort(Arr=[10,1,2,4,5,7,4]):
	start = time.time()
	n= len(Arr)
	c=0
	for i in range (0,n):
		for j in range(0,n-i-1):
			c=c+1
			if Arr[j] > Arr[j+1]:
				Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
	end = time.time()
	print("BubbleSort: "+str(end - start))
	return Arr
		
#Bubble()

