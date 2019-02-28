#Iterative MergeSort
import random
def merge (a,l,m,r):#Utility fn to sort subarrays
	n1 = m - l + 1
	n2 = r - m
	L = [0] * n1
	R = [0] * n2
	for i in range (0,n1):
		L[i] = a[l+i]
	for i in range (0,n2):
		R[i] = a[m+i+1]
	i , j , k = 0 , 0 , l
	while i < n1 and j < n2: 
		if L[i] > R[j]: 
			a[k] = R[j] 
			j += 1
			print ('{0}'.format(j))
		else: 
			a[k] = L[i] 
			i += 1
		k += 1
	while i<len(L):
		a[k] = L[i]
		i+=1
		k+=1
		while j<len(R):
			a[k] = R[j]
			j+=1
			k+=1
def mergeSort(a):
	curr_size = 1
	while curr_size < len(a) - 1:
		left = 0 
		while left < len(a) - 1:
			mid = left + curr_size -1
			right = ((left+ 2 * curr_size -1),len(a)-1)[(left + 2 *curr_size -1) > len(a) -1]
			merge(a, left, mid, right)
			left = left + curr_size * 2 
		curr_size *= 2 

a = []
for c in range (10000000):
	a.append(random.randint(0, 100000000))

#a = [5,2,1,6,7,3,4,9]
#mergeSort(a)
#for num in a :
#	print (num, end = " ")

