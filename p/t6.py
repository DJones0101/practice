'''
If you're given 3 arrays, write an algorithm that gives you all the common elements from the arrays.

Example:

Array 1: [1,3,5,3,0]

Array 2: [0,5,3,3,13,10]

Array 3: [3,7,11,5,3,0,9]

Output: [3,5,0]
'''


def getCommon(a, b, c):

	#T: O(a + b + c), S:O(n)

	result = []
	hashMap = {}

	for num in a:
		if num not in hashMap:
			hashMap[num] = []

	for num in b:
		if num in hashMap:
			hashMap[num].append(1)

	for num in c:
		if num in hashMap:
			hashMap[num].append(1)

	for key, val in hashMap.items():

		if len(val) >= 2:
			result.append(key)

	return result


a = [1,3,5,3,0]
b = [0,5,3,3,13,10]
c = [3,7,11,5,3,0,9]

r = getCommon(a, b, c)

check = "The common numbers between\n {}\n {}\n {}\n \n\nare {}\n\n".format(a,b,c,r)

print(check)