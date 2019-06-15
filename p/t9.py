

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return  self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def peek(self):
		end = len(self.items) - 1
		return self.items[end]

	def size(self):
		return len(self.items)

	def display(self):
		print("{}".format(self.items))


def isVaild(string):


	'''
	Given a string with parenthesis, determine whether the parenthesis are balanced or not. You can assume that there are only three types of parenthesis - (), {} and [].

	Example: 

	Input = '({}[])' Output = true

	Input = '({]})' Output = false

	'''
	open_st = ['(','{','[']
	close_st = [')','}',']']

	stack = Stack()

	for char in string:

		if char in open_st:

			stack.push(char)

		elif char in close_st:

			index = close_st.index(char)

			if stack.peek() == open_st[index] and stack.isEmpty() == False:
				stack.pop()
			else:
				return False
	return True



b = '([{}])'
n = '({[[})'

balanced = "Is {} balanced {}".format(b,isVaild(b))
notBalanced = "Is {} balanced {}".format(n, isVaild(n))

print(balanced)
print(notBalanced)





