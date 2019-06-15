
class Node:
	def __init__(self, data=None, nextNode=None):
		self.data = data
		self.next = nextNode


class LinkedList:

	def __init__(self):
		self.head = Node()
		self.length = 0

	def append(self, data):
		new_node = Node(data)
		curr = self.head

		while curr.next != None:
			curr = curr.next

		self.length += 1
		curr.next = new_node

	def get_length(self):
		return  self.length


	def display(self):
		curr = self.head
		cache = []
		while curr.next != None:
			curr = curr.next
			cache.append(curr.data)

		print (cache)
		return 

	def get_index(self, index):

		# indexing will start at 0
		if index > self.get_length() or index < 0:
			raise  ValueError("Index out of bounds")
			
		else:
			count = 0
			curr = self.head
			while curr.next != None:
				curr = curr.next
				if count == index:
					return curr.data
				else:
					count += 1

	def insert(self, data, index):

		new_node = Node(data)
		if index < 0 or index > self.length:

			raise ValueError("Index out of bounds")
			
		elif index == 0: #first node

			new_node.next = self.head.next
			self.head.next = new_node
			self.length += 1
			return 
		elif index == self.length: #last node

			curr = self.head
			while curr.next != None:
				curr = curr.next

			new_node.next = curr
			curr.next = new_node
			return 

		else: # between

			curr = self.head
			count = 0
			self.length += 1
			while curr.next != None:
				curr = curr.next
				count += 1

				if count ==  index:
					new_node.next = curr.next
					curr.next = new_node
					return


	def delete_index(self, index):

		if index > self.length or index < 0:
			raise ValueError("Index out of bounds")
		
		else:
			count = -1
			curr = self.head
			self.length -= 1

			if index == self.length :

				while curr.next != None:
					prev = curr
					curr = curr.next

				prev.next = None

			else:

				while curr.next != None:

					prev = curr
					curr = curr.next
					count += 1

					if index == count:
						prev.next = curr.next
						return

	def reverse_list(self):
		'''
		Given a linked list, reverse the linked list in an optimal way.

		For example, if the input linked list is [1,2,3,4], then your algorithm should return '[4,3,2,1]'.
		'''	

		curr = self.head.next
		prev = None
		
		while curr != None:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node

		self.head.next = prev
		return 

mylist = LinkedList()

for i in range(1, 5):
	mylist.append(i)

mylist.display()
print("\n")
mylist.reverse_list()
mylist.display()	



