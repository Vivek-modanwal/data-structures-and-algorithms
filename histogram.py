
def boundary(A,start,end):
	if start==end:
		return A[start]

	mid=(start+end)//2
	b1=boundary(A,start,mid)
	b2=boundary(A,mid+1,end)
	return merge(b1,b2)

def merge(b1,b2):
	i,j=0,0
	b3=[]
	if b1[0] < b2[0]:
		b2=[b1[0],0]+b2
	elif b1[0] > b2[0]:
		b1=[b2[0],0]+b1
	if b1[-1] < b2[-1]:
		b1=b1+[0,b2[-1]]
	elif b1[-1] > b2[-1]:
		b2=b2+[0,b1[-1]]
	while i<len(b1)-1 and j<len(b2)-1:
		H=max(b1[i+1],b2[j+1])
		if (len(b3)>0 and b3[-1]!=H) or len(b3)==0:
			b3.append(b1[i])
			b3.append(H)
		if b1[i+2]<b2[j+2]:
			i+=2
			b2[j]=b1[i]
		elif b1[i+2]>b2[j+2]:
			j+=2
			b1[i]=b2[j]
		else:
			i+=2
			j+=2

	b3.append(b1[i])
	return b3


def Histogram_boundary(A):
	return boundary(A,0,len(A)-1)


A=[[3,13,9],[1,11,5],[12,7,16],[14,3,25],[19,18,22],[2,6,7],[23,13,29],[23,4,28]]
print(Histogram_boundary(A))