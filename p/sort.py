import random


def  merge(left, right):
	result = []
	i, j = 0, 0

	while i < len(left) and j < len(right):

		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[j:])
	return  result

	
def mergesort(seq):

	# T: O(n log n), S: O(n), not in place

	size = len(seq)
	
	if size < 2:
		return  seq
	else:
		middle = size // 2
		left = mergesort(seq[:middle])
		right = mergesort(seq[middle:])
		return merge(left, right)



def partition(seq, start, end):

	pivot = seq[end]
	left = start
	right = end -1
	
	while left <= right:

		while left <= end and seq[left] < pivot:
			left += 1

		while right >= start and seq[right] >= pivot:
			right -= 1

		if left < right:
			seq[right], seq[left] = seq[left], seq[right]
		else:
			seq[end], seq[left] = seq[left], seq[end]

	return left


def quicksort(seq, start, end):

	# T: O(n log n), S: O(1) in place
	if start >= end:
		return 
	else:	
		middle = partition(seq, start, end)
		quicksort(seq, start, middle - 1)
		quicksort(seq, middle + 1, end)
		


def _quicksort(seq):

	# T: O(nlogn), S: O(n), not in place

	if len(seq) < 2:
		return seq
	else:
		pivot = random.choice(seq)
		smaller = [i for i in seq if i < pivot]
		bigger = [i for i in seq if i > pivot]
		return _quicksort(smaller) + [pivot] + _quicksort(bigger)

	


l = [23,500, 43, 65, 34, 28, 654]
q = [43, 243, 454, 7657, 56, 3, 3457] 
l = mergesort(l)
quicksort(q, 0, len(q)-1)

print("Mergesort : {}".format(l))
print("Quicksort : {}".format(q))
k = [25,40,78,56,73,150,280,2001,1991] 
j = _quicksort(k)
print("_Quicksort : {}".format(j))

