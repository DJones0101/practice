'''

Shift every element of an array over by k number of spaces, 
for example arr = [a, b, c, d, e] k = 2, [d, e, a, b, c] should be returned 

'''


def shift_by_k(arr, k):

	# T: O(n) S: O(n)
	
	hash_table = {key : value for key , value in enumerate(arr) }
	size = len(arr) 

	for i in range(size):

		j = (i + k) % size

		arr[j] = hash_table[i]

	return  arr

arr1 = ['a', 'b', 'c', 'd', 'e',] 
k = 2
shift_by_k(arr1, k)

check1 = "is {} shifted by  {} spaces?".format(arr1, k)
print(check1)
