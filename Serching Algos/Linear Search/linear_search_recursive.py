#This is an implementation of the 'Linear Search' Algorithm in Python Programming Language.

#Implementation of Linear Search by the use of Recursion-
def linear_search(arr,ele):
	for i in range(len(arr)):
		if arr[i]==ele:
			return(i) #"Given element found at",i,"th index in the given array.") #following 0-based indexing
	return-1

print(linear_search([1,3,52,4,5,44,11],5))
print(linear_search([1,3,52,4,5,44,11],55))
