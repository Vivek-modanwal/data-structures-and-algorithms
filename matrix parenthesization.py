import math
def costof_multiplication(A,start,end,lookup,order):
	if start==end:
		lookup[start][end]=0
		order[start][end]=-1
		return 0
	Min=math.inf
	temp=0
	index=0
	for i in range(start,end):
		temp=costof_multiplication(A,start,i,lookup,order)+costof_multiplication(A,i+1,end,lookup,order)+(A[start][0]*A[i][1]*A[end][1])
		if temp<Min:
			Min=temp
			index=i
	lookup[start][end]=Min
	order[start][end]=index
	return Min

def get_order(order,start,end):
	if start==end:
		return 'A'+str((start+1))
	left=get_order(order,start,order[start][end])
	right=get_order(order,order[start][end]+1,end)
	return '('+left+'.'+right+')'

if __name__=='__main__':
	
	A=[[5,4],[4,3],[3,10],[10,7],[7,1]]
	temp=[0]*len(A)
	lookup=[]
	for i in range(len(A)):
		lookup.append(temp.copy())
	order=[]
	for i in range(len(A)):
		order.append(temp.copy())
	print(costof_multiplication(A,0,len(A)-1,lookup,order))
	print(get_order(order,0,len(A)-1))

	for  x in lookup:
		print(x)