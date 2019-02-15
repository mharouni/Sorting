#MergeSort

def merge(Arr=[19,29,17,2,4,3,100,1]):
	if len(Arr)>1:
		mid = len(Arr)//2
		L= Arr[:mid]
		R = Arr[mid:]
		merge(L)
		merge(R)
		i = j = k = 0
		
		while i < len(L) and j < len(R):
			print('{0},{1},{2}'.format(i,j,k))
			if L[i] < R[j]:
				Arr[k] = L[i]
				i+=1
				k+=1
			else:
				Arr[k] = R[j]
				j+=1
				k+=1

		while i < len(L):
			Arr[k] = L[i] 
			i+=1
			k+=1

		while j < len(R): 
			Arr[k] = R[j]
			j+=1
			k+=1


		for h in range(len(Arr)):
			print(Arr[h],end = ' ')

merge()