import numpy as np
from sympy import Matrix

def lfsr(seed, vektor):
	firstseed = seed[:]
	state_array = []
	print(seed)
	state_array.append(firstseed)
	p = 0
	a = ""
	if (len(vektor)!=len(seed)):
		print("Len Seed: "+str(len(seed))+"Len Vektor: "+ str(len(vektor)))
		return

	while True:
		b = 0
		for i in range(len(seed)-1,-1,-1):
			if (vektor[i] == 1):
				b ^= seed[i]
		a+=str(seed.pop())
		seed.insert(0,b)
		print(seed)
		p +=1
		for i in range(len(state_array)):
			if (state_array[i]==seed):
				print("Length of the Keystream")
				print(p)
				print("Sequence:")
				print(a)
				return a
		state_array.append(seed[:])


def matrix(sequence,deg):
	if (len(sequence)/deg < 2):
		return 0
	if isinstance(sequence,str):
		sequence_a = list(sequence)

	ma = [[0]*deg]*deg
	for i in range(deg):
		ma[i] = sequence_a[i:deg+i][:]
	a = Matrix(ma)
	x = np.array(a.inv_mod(2)) 
	b = np.array(list(map(int,sequence[deg:][:])))
	x = np.flip(x.dot(b)%2)
	print("feedback coefficients:")
	return x

#Example
x = "1010000110111011"
deg = 8
y = matrix(x,deg)
print(y)
lfsr(list(map(int,(reversed(x[:deg])))),y)
