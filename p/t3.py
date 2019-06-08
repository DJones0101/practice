'''
If you're given a sentence, how would you reverse the entire sentence without reversing each word?

For example, if the input is 'I love California', then your algorithm should return 'California love I'.
'''


def reverse(arr):

	# T: O(n), S: O(n)

	for i, char in enumerate(arr[::-1]):
		arr[i] = char

	hash_table = {}
	count = 0
	start = 0
	for end, char in enumerate(arr):
		if char == " ":
			hash_table[count] = arr[start:end]
			start = end
			count += 1
		elif end == len(arr) - 1:
			hash_table[count] = arr[start:end + 1]

	new_arr = []
	for key, val  in hash_table.items():
		for i, char in enumerate(val[::-1]):
			new_arr.append(char)
		new_arr.append(" ")

	return  new_arr
		

arr = ['i',' ','l', 'o', 'v', 'e',' ','c','a','l','i','f','o','r','n','i','a',]
print("".join(arr))
new_arr = reverse(arr)
print("".join(new_arr))
