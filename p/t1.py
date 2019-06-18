'''

Shift every element of an array over by k number of spaces, 
for example arr = [a, b, c, d, e] k = 2, [d, e, a, b, c] should be returned 

'''


def shift_by_k(arr, k):

	# T: O(n) S: O(n)
	return arr[k:] + arr[:k]

arr1 = ['a', 'b', 'c', 'd', 'e',] 
k = 2
arr1 = shift_by_k(arr1, k)

check1 = "is {} shifted by  {} spaces?".format(arr1, k)
print(check1)
