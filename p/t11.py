'''
Implement a queue using stacks.
'''

class Queue:

	def __init__(self):
		self.s1 = []
		self.s2 = []
		self.top = None

	def pop(self):
		while self.s1:
			self.s2.append(self.s1.pop())

		res = self.s2.pop()
		self.top = self.s2[len(self.s2)-1]

		while self.s2:
			self.s1.append(self.s2.pop())

		return res

	def push(self, data):
		self.s1.append(data)
		if len(self.s1) == 1:
			self.top = self.s1[0]
		

	def peek(self):
		return self.top

	def isEmpty(self):
		return self.s1 == []

	def display(self):
		print("{}".format(self.s1))


myQ = Queue()
for i in range(1,11):
	myQ.push(i)

peek = "peek {}".format(myQ.peek())
print(peek)
myQ.display()
myQ.pop()
peek = "peek {}".format(myQ.peek())
print(peek)
myQ.display()
myQ.pop()
myQ.pop()
peek = "peek {}".format(myQ.peek())
print(peek)
myQ.display()

