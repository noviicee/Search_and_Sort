#This implementation of quick-sort is the simplest way to understand how a quick sort algorithm actually works.

def quick_sort_basic(arr):
#arr is the given array to be sorted

	if len(arr)<=1:
		return arr
	"""this is the base case, for the moment when 1 element, or no element will be present in the array
	also, one such case would be when the pivot element will be the largest. For an example-
	arr=[1,2,3]
	in such cases, when we will be calling on quick_sort_basic(right), there won't be any element present in the right array,
	so we need to add len==0 case also"""


	pivot=arr.pop()
	left=[]
	right=[]

	for item in arr:
		if item<pivot:
			left.append(item)
		else:
			right.append(item)

	"""the items smaller than the pivot element are added to the left subarrray, and the elements greater than the pivot elements are added to the right subarray"""

	return(quick_sort_basic(left)+[pivot]+quick_sort_basic(right))
	#the above process is repeated until there is just one element, or no element left in the original array

	"""Here, we are adding pivot since if we don't do it manually, the pivot element willjust be eliminated after every loop execution"""

#finally the result is returned and printed as per user's approach

print(quick_sort_basic([1,21,12,32,43,23,4]))