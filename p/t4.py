'''
If you're given an array of numbers and a number, you have to find the set of 2 elements that sum up to given number?

For example, if the inputs are: [2,4,1,9,7] & 9, then your algorithm should return '[2,7]'.
'''

def find_sum(arr, n):

	# T: O(n^2), S:O(n)

	hashMap = {}

	for i in range(len(arr)):
		for j in range(len(arr)):

			val = arr[i] + arr[j]
			hashMap[val] = (arr[i], arr[j])

	return  hashMap[n]


arr = [2,4,1,9,7]
n = 9
check = "{} can be computed using  {}".format(n, find_sum(arr,n))
n = 5
check1 = "{} can be computed using  {}".format(n, find_sum(arr,n))
n = 16
check2 = "{} can be computed using  {}".format(n, find_sum(arr,n))

print(check)
print(check1)
print(check2)