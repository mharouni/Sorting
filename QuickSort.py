#QuickSort
import random
def part(arr,low,high):
	pivot = arr[high]
	i = low - 1 #i is the variable corresponding to the latest index less than the pivot
	for j in range (low, high):
		if arr[j] <= pivot:
			i +=1
			arr[i],arr[j] = arr[j],arr[i]


	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return i+1

def QuickSort(arr,low,high):
	if low < high:
		
		pi = part(arr, low, high)
		QuickSort(arr, low, pi - 1)
		QuickSort(arr, pi +1, high)

'''		
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
QuickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
'''
arr = []
for c in range (100000):
	arr.append(random.randint(0, 1000000))


QuickSort(arr, 0, len(arr) - 1)
print('d')
