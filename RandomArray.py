#RandomArray
import random
def Gen(n=10000):
	Arr = []
	for c in range(n):
		Arr.append(random.randint(0,n*10))
	return Arr
#print(Gen(10))