

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return  self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		end = len(self.items) - 1
		return self.items[end]

	def size(self):
		return len(self.items)

	def display(self):
		print("{}".format(self.items))


def isVaild(string):


	'''
	Given a string with parenthesis, determine whether the parenthesis are balanced or not.
	You can assume that there are only three types of parenthesis - (), {} and [].

	Example: 

	Input = '({}[])' Output = true

	Input = '({]})' Output = false

	'''
	open_st = ['(','{','[']
	close_st = [')','}',']']

	# T: O(n), S: O(n)

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

def swap(start, end, string):

	while start < end:
		string[start], string[end] = string[end], string[start]
		start += 1
		end -= 1
	


def reverse(string):

	start = 0
	end = 0

	string = list(string)

	for i in range(len(string)):

		if string[i] == " " and i == 1:
			pass
		elif string[i] == " ":
			
			end = i
			swap(start, end, string)
			start = end

		elif i == len(string) - 1:
			end = i
			swap(start, end, string)

	stak = Stack()
	j = 0

	while j != len(string) - 1:
		stak.push(string[j])
		j += 1

	j = 0 

	while stak.isEmpty() == False:
		string[j] = stak.pop()
		j += 1

	return "".join(string)



	



# b = '([{}])'
# n = '({[[})'

# balanced = "Is {} balanced {}".format(b,isVaild(b))
# notBalanced = "Is {} balanced {}".format(n, isVaild(n))

# print(balanced)
# print(notBalanced)

string = 'I Love California'

print("Original : {}".format(string))
string = reverse(string)
print("Revesered : {}".format(string))

string1 = "we hate cold"

print("Original : {}".format(string1))
string1 = reverse(string1)
print("Revesered : {}".format(string1))



