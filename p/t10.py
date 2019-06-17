'''
Implement a Stack using only one Queue.
'''

class Stack:

	def __init__(self):
		self.itmes = []
		self.size = 0
		self.top = None

	def push(self, data):
		self.top = data
		self.size += 1
		self.itmes.append(data)

	def pop(self):

		if self.itmes[0] == self.top:
			self.size -= 1
			return self.itmes.pop(0)
		else:
			temp = self.itmes.pop(0)

			while self.top != temp:
				self.size -= 1
				self.itmes.append(temp)
				temp = self.itmes.pop(0)
			self.top = self.itmes[len(self.itmes)-1]
			return temp
	
	def peek(self):
		return self.top

	def size(self):
		return self.size

	def isEmpty(self):
		return self.itmes == []

	def display(self):
		print("{}".format(self.itmes))



stak = Stack()
for i in range(1,11):
	stak.push(i)
	
stak.display()
stak.pop()
stak.pop()
stak.display()
print("peek {}".format(stak.peek()))
stak.pop()
stak.pop()
stak.display()
print("peek {}".format(stak.peek()))
print("is empty {}".format(stak.isEmpty()))
