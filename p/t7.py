'''
Give an array of integers and an integer k, find all subsets of that array that sum to the number k.

This problem was difficult, I need to spend some time looking before I move on.
'''


def perfectSum(arr, ksum):


	def _perfectSum(arr, size, subset, ksum):

		if ksum == 0:
			for value in subset:
				print(value, end=' ')
			print()
			return 
		if size == 0:
			return 

		_perfectSum(arr, size - 1, subset, ksum)
		subset1 = [] + subset
		subset1.append(arr[size - 1])
		_perfectSum(arr, size - 1, subset1, ksum - arr[size-1])

	size = len(arr) 
	subset = []
	_perfectSum(arr, size, subset,ksum)




	

arr = [1,3,5,0]
ksum = 6

perfectSum(arr,ksum)