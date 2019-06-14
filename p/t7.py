'''
Give an array of integers and an integer k, find all subsets of that array that sum to the number k.

This problem was difficult, #come back to this one#. This is a dynamic programming problem w/ memoization.
'''


def perfectSum(arr, ksum):

	# T: O(2^n) S: O(n)

	def _perfectSum(arr, size, subset, ksum,  cache):

		if ksum == 0:
			cache.append(subset)
			return 
		if size == 0:
			return 

		_perfectSum(arr, size - 1, subset, ksum, cache)
		subset1 = [] + subset
		subset1.append(arr[size - 1])
		_perfectSum(arr, size - 1, subset1, ksum - arr[size-1],  cache)

	size = len(arr) 
	subset = []
	cache = []

	_perfectSum(arr, size, subset,ksum,  cache)

	return cache


cache =[0, 1]
def fib(n):

	if n < 0:
		print("n must be a positive integer")

	elif n <= len(cache):
		return cache[n -1 ]
	else:
		temp = fib(n - 1) + fib(n - 2)
		cache.append(temp)
		return temp 



	

arr = [1,3,5,0,]
ksum = 6

print(perfectSum(arr,ksum))

print("9 : {}".format(fib(9)))

