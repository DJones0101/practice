'''
If you're given an array of numbers, find out the length of the longest consecutive subsequence in that array.

For example, if the input is [2,1,6,9,4, 3], then your algorithm should return 4 because the longest 
subsequence in that array is [1,2,3,4].

'''

def longest_subseq(arr):

	# T: O(n ^ 2), S: O(n)

	hashMap = {num : [] for num in arr}	
	
	for key, val in hashMap.items():

		for i in range(len(arr)):
			cur = key + i
			
			if cur in hashMap:
				
				if hashMap[key] == []:
					hashMap[key].append(key)

				elif cur - val[-1] == 1:
					 hashMap[key].append(cur)

	largest_val = 0


	for key, val in hashMap.items():
		size = len(val)
		if(size  > largest_val):
			largest_val = size
			

	return largest_val


arr = [2,1,6,9,4,3,]
arr1 = [2,11,8,1,6,13,9,10,4,3,12]
check = "The longest subsequnce in {} is {}".format(arr, longest_subseq(arr))

check1 = "The longest subsequnce in {} is {}".format(arr1, longest_subseq(arr1))

print(check)
print(check1)


