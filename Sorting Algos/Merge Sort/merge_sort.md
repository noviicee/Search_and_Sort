Merge Sort
----------
----------

The Merge Sort works on the concept of *Divide and Conquer*

This technique divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.


If we go deeper in this, there can be two possible implementations-

a)[The first approach](#), can be to make a separate array, which contains the elements in a sorted manner.

b)[The second appproach](#), can be to modify the given array itself.
In this approach, the space-complexity would be less as compared to the first approach, since we are modifying the array itself, and are not creating any new array.

Broadly,in this particular [implementation of merge sort](#), the *merge()* function is used for merging two halves, and the key function, i.e, *merge_sort()* is used to basically follow the *divide* algorithm of the *divide and conquer*.


**Details-**

Inventor: John von Neumann [Know This Person](https://en.wikipedia.org/wiki/John_von_Neumann)

Worst complexity: n'\*'log(n)

Average complexity: n'\*'log(n)

Best complexity: n'\*'log(n)

Space complexity: n

Stable: Yes [Stable Algorithm](#)

#Note: here **n** is considered as the size of the given array