def merge_sort(arr):
	if len(arr)==0 or len(arr)==1:
		return arr

	mid=len(arr)//2

	l1=arr[:mid]
	l2=arr[mid:]

	merge_sort(l1)
	merge_sort(l2)

	return merge(l1,l2)

def merge(l1,l2):
	l=[]
	i=j=0
	while i<len(l1) and j<len(l2):
		if l1[i]<l2[j]:
			l.append(l1[i])
			i+=1
		else:
			l.append(l2[j])
			j+=1

	while i<len(l1):
		l.append(l1[i])
		i+=1

	while j<len(l2):
		l.append(l2[j])
		j+=1

	return l


print(merge_sort([4,6,3,1]))