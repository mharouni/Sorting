#InsertionSort
import time
def sort(Arr=[1,2,34,4,5,6,7]):
	start = time.time()
	n=len(Arr)
	for i in range(1,n):
		temp = Arr[i]
		j=i
		while j>=0 and temp < Arr[j-1]:
			Arr[j] = Arr[j-1]
			j-=1
		Arr[j] = temp
	end = time.time()
	print("InsertionSort: "+str(end - start))
	return Arr

#print(Insertion())
			