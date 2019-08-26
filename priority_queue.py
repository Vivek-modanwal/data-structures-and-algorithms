class priorityQueue:

	@staticmethod
	def insert(heap,data,key=None):
		heap.append(data)
		if key:
			key[data[1]]=len(heap)-1
		priorityQueue.percolateUp(heap,len(heap)-1,key)

	@staticmethod
	def extractMin(heap,key=None):
		
		if key:
			key.pop(heap[0][1])
			key[heap[-1][1]]=0
		heap[0]=heap[-1]
		heap.pop()
		if len(heap)>1:
			priorityQueue.heapify(heap,0,key)

	@staticmethod
	def findMin(heap):
		if len(heap):
			return heap[0]

	@staticmethod
	def BuildPQ(heap,key=None):
		index=(len(heap)//2)-1
		if index<0:
			return
		for i in range(index,-1,-1):
			priorityQueue.heapify(heap,i,key)


	@staticmethod
	def heapify(heap,index,key=None):
		smallest=index
		if 2*index+1<len(heap) and heap[2*index+1][0]<heap[smallest][0]:
			smallest=2*index+1
		if 2*index+2<len(heap) and heap[2*index+2][0]<heap[smallest][0]:
			smallest=2*index+2
		if smallest!=index:
			if key:
				temp=key[heap[index][1]]
				key[heap[index][1]]=key[heap[smallest][1]]
				key[heap[smallest][1]]=temp

			temp=heap[index]
			heap[index]=heap[smallest]
			heap[smallest]=temp
			priorityQueue.heapify(heap,smallest,key)


	@staticmethod
	def decreaseKey(heap,index,data,key=None):
		if heap[index][0]>data:
			heap[index][0]=data
			priorityQueue.percolateUp(heap,index,key)
		

	@staticmethod
	def percolateUp(heap,index,key):
		if index==0:
			return
		parent=(index-1)//2
		if heap[parent]>heap[index]:
			if key:
				temp=key[heap[parent][1]]
				key[heap[parent][1]]=key[heap[index][1]]
				key[heap[index][1]]=temp
				# key[heap[parent][1]]=index
				# key[heap[index][1]]=parent
			temp=heap[parent]
			heap[parent]=heap[index]
			heap[index]=temp
			priorityQueue.percolateUp(heap,parent,key)

	