n=int(input())
x=1
A=[1]
for i in range(1,n+1):
	for j in range(n-i):
		print('   ',end='')
	for j in range(i):
		print(f'{A[j]:^3}   ',end='')
	print()
	B=[]
	B.append(1)
	for j in range(1,len(A)):
		B.append(A[j]+A[j-1])
	B.append(1)
	A=B