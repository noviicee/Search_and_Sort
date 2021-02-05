#This is an implementation of the 'Binary Search' Algorithm in Python Programming Language.

#Implementation of Binary Search by the use of Recursion-
def binary_search(arr,ele,si,ei):
#make sure that the given array is sorted
#si= Starting index of the list
#ei= End index of the list
#here, the 1-based indexing is used; user can chose any indexing as he/she likes; in some cases, modification may be reqquired.
	mid=(si+ei)//2 #calculating the middle index
	if si>ei:
		print("Given element not found in the list.")
		return(-1)
	if arr[mid]==ele:
		return mid
	if arr[mid]>ele:
		return(binary_search(arr,ele,si,mid-1))
	return(binary_search(arr,ele,mid+1,ei)) #eventually returns the index of the element in the list

print(binary_search([1,2,3,4,5,6,8,9,66],58,1,9))
	