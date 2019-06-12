'''
Given an input array, reverse it in O(n) time complexity and O(1) space complexity.
'''

def swap(arr, start, end):

	while start < end:
		 arr[start], arr[end] = arr[end], arr[start]

		 start += 1
		 end -= 1


a = [1,3,5,3,0]
b = [0,5,3,3,13,10]
c = [3,7,11,5,3,0,9]

check = "{} reveserd is ".format(a)
swap(a, 0, len(a)-1)
ar = "{}".format(a)
check = check + ar


check1 = "{} reveserd is ".format(a)
swap(b, 0, len(b)-1)
br = "{}".format(b)
check1 = check1 + br

check2 = "{} reveserd is ".format(a)
swap(c, 0, len(c)-1)
cr = "{}".format(c)
check2 = check2 + cr

print(check)
print(check1)
print(check2)
