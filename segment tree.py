import math
class segmentTree:
	def __init__(self,li):
		self.list=li
		self.tree=[0]*(4*len(li)-3)
		self.__construction(0,len(li)-1,0)

	def __construction(self,start,end,index):
		if start==end:
			self.tree[index]=self.list[start]
			return
		mid=(start+end)//2
		self.__construction(start,mid,2*index+1)
		self.__construction(mid+1,end,2*index+2)
		self.tree[index]=min(self.tree[2*index+1],self.tree[2*index+2])
		return

	def __RMQ(self,l,r,start,end,index):#range minimum query
 		if r<start or l>end:
 			return math.inf
 		if start>=l and end<=r:
 			return self.tree[index]
 		mid=(start+end)//2
 		left=self.__RMQ(l,r,start,mid,2*index+1)
 		right=self.__RMQ(l,r,mid+1,end,2*index+2)
 		return min(left,right)

	def rangeMin(self,start,end):
 		return self.__RMQ(start,end,0,len(self.list)-1,0)	



print(dir(segmentTree))
l=[1,2,3,4,5,6]
st=segmentTree(l)
for i in range(len(l)):
	for j in range(i,len(l)):
		print(st.rangeMin(i,j))

