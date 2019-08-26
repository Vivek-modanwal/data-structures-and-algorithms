def median_of_medians(A):
	if len(A)<6:
		A.sort()
		return A[len(A)//2]


	B=[]
	for i in range(0,len(A),5):
		C=A[i:i+5]
		B.append(C[len(C)//2])
	return median_of_medians(B)
