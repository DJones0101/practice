
class Node(object):
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

	def get_index(self, index):

		# indexing will start at 0
		if index > self.get_length() or index < 0:
			print("Index out of bounds")
			return
		else:
			count = 0
			curr = self.head
			while curr.next != None:
				curr = curr.next
				if count == index:
					return curr.data
				else:
					count += 1

	def insert(self, data):

		pass

	def delete_index(self, index):

		if index > self.length or index < 0:
			print("index out of bounds")
			return 
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

		


mylist = LinkedList()

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

mylist.display()



mylist.delete_index(3)
mylist.display()
print(mylist.get_length())

