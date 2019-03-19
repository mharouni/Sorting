#SelectionSort
import time
def sort(Arr=[4,3,2,1,10,8,6,5]):
	start = time.time()
	n=len(Arr)
	for i in range(0,n-1):
		m =i
		for j in range(i+1,n):
			if Arr[j] < Arr[m]:
				m = j
		#print(m)
		Arr[i],Arr[m] = Arr[m],Arr[i]
	end = time.time()
	print("SelectionSort: "+str(end - start))
	return Arr
	

			
