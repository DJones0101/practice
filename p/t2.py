'''
If you're given an array in which the value at each index is a reference to the next index, how do you find whether it has a cycle or not?

For example, if the input array is [1,2,4,5,3,6,3,8], then your algorithm should return 'true'.

'''


def has_cycle(arr):
	
	# T: O(n), S: O(1)

	turtle = arr[0]
	rabbit = arr[0]
	size = len(arr) - 1

	while True:

		turtle = arr[turtle]
		rabbit = arr[rabbit]
		rabbit = arr[rabbit]

		if turtle == rabbit:
			return True	
		elif turtle > size or rabbit > size:
			return False


def _has_cycle(arr):
	
	# T: O(n),  S:O(n)
	size = len(arr)
	hash_table = {i : 0 for i in range(size)}

	for item in arr:
		if item < size:
			hash_table[item] = hash_table[item] + 1

	for key, value in hash_table.items():
		if value > 1:
			return True

	return  False

arr1 =  [1,2,1,3,4,8,]
arr2 =  [1,2,3,4,5,]
arr3 =  [1,2,4,5,3,6,3,8]

check1 = " does {} have a cycle? {}".format(arr1, has_cycle(arr1))
check2 = " does {} have a cycle? {}".format(arr2, has_cycle(arr2))
check3 = " does {} have a cycle? {}\n\n".format(arr3, has_cycle(arr3))

print(check1)
print(check2)
print(check3)

check1 = " does {} have a cycle? {}".format(arr1, _has_cycle(arr1))
check2 = " does {} have a cycle? {}".format(arr2, _has_cycle(arr2))
check3 = " does {} have a cycle? {}".format(arr3, _has_cycle(arr3))

print(check1)
print(check2)
print(check3)

