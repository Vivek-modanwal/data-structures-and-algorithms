# Disjoint set using Union by rank and path compression

# path compression :-It speeds up the data structure by
# compressing the height of the trees. It can be achieved
# by inserting a small caching mechanism into the Find operation.



class disjoint_set:

	def __init__(self,n):
		self.size=n
		self.create_set()

	def create_set(self):
		self.set=[i for i in range(self.size)]
		self.rank=[1 for i in range(self.size)]

	def find_set(self,x):
		if self.set[x]==x:
			return x
		intermediate=self.find_set(self.set[x])
		self.set[x]=intermediate#path compression
		return intermediate


	def union(self,x,y):
		s1=self.find_set(x)
		s2=self.find_set(y)
		if s1==s2:
			return
		#union by rank
		if self.rank[s1]<self.rank[s2]:
			self.set[s1]=s2

		elif self.rank[s1]>self.rank[s2]:
			self.set[s2]=s1

		else:
			self.set[s2]=s1
			self.rank[s1]+=1

if __name__=='__main__':		
	data=[[0,1,1],[0,4,3],[1,4,4],[3,4,5],[1,3,6],[1,2,7],[2,3,2]]
	newdata=[]
	data.sort(key=lambda x : x[2])
	ds=disjoint_set(len(data))
	for d in data:
		x=ds.find_set(d[0])
		y=ds.find_set(d[1])
		if x!=y:
			newdata.append(d)
			ds.union(x,y)
	print(newdata)

