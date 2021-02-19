
def merge_sort(l):
	if len(l)==0 or len(l)==1:
		return l
	mid=len(l)//2
	l1=l[:mid]
	l2=l[mid:]
	merge_sort(l1)
	merge_sort(l2)

	merge(l1,l2,l)
	return l

def merge(l1,l2,l):
	i,j,k=0,0,0
	while i <len(l1) and j<len(l2):
		if l1[i]<l2[j]:
			l[k]=l1[i]
			i+=1
			k+=1
		elif l1[i]>l2[j]:
			l[k]=l2[j]
			j+=1
			k+=1
	while i <len(l1):
		l[k]=l1[i]
		k+=1
		i+=1
	while j<len(l2):
		l[k]=l2[j]
		k+=1
		j+=1
        
print(merge_sort([1,3,5,2,4,6,8]))