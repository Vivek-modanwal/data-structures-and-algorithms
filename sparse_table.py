import math
def sparse_table(A):
	N=len(A)
	M=math.floor(math.log2(N))+1
	temp=[0]*N
	table=[temp.copy() for _ in range(M)]
	for i in range(M):
		for j in range(N-2**i+1):
			if i==0:
				table[i][j]=A[j]
			else:
				table[i][j]=min(table[i-1][j:j+2**(i-1)+1])
	return table

if __name__=='__main__':
	A=[2,4,3,1,6,7,8,9]
	table=sparse_table(A)
	l=0
	u=0
	len=u-l+1
	x=math.floor(math.log2(len))
	print(max(table[x][l],table[x][u-2**x+1]))