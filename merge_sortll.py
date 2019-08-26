class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Linkedlist:
	def __init__(self):
		self.head = None

	def append(self,data):
		temp=Node(data)
		temp.next=self.head
		self.head=temp


	def print(self):
		temp = self.head
		while(temp!=None):
			print(temp.data,end=' ')
			temp = temp.next
		print()


def mergesort(head,end):
	fast = head
	slow = head

	if head.next==end:
		head.next=None
		return head

	while (fast != end and fast.next!=end):
		fast = fast.next.next
		slow=slow.next

	left=mergesort(head,slow)
	right=mergesort(slow,end)
	return merge(left,right)

	
def merge(left,right):
	head = None
	tail = None

	while(left !=None and right !=None):
		if(left.data<right.data):
			if(head==None):
				head = left
				tail = left
			else:
				tail.next = left
				tail = left
			left = left.next
		else:
			if(head==None):
				head = right
				tail = right
			else:
				tail.next = right
				tail = right
			right = right.next
	if left!=None:
		tail.next=left
	if right!=None:
		tail.next=right

	return head






List=Linkedlist()
for i in range(10):
	List.append(i)
print('Before sorting')
print('-'*50)
List.print()
List.head=mergesort(List.head,None)
print('\nBfter sorting')
print('-'*50)
List.print()
