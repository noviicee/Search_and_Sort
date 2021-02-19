Merge Sort
----------
----------

The Merge Sort works on the concept of *Divide and Conquer*

This technique divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.


If we go deeper in this, there can be two possible implementations-

a)[The first approach](https://github.com/noviicee/Search_and_Sort/blob/main/Sorting%20Algos/Merge%20Sort/merge_sort_1.py), can be to make a seperate array, which contains the elements in a sorted manner.

b)[The second appproach](https://github.com/noviicee/Search_and_Sort/blob/main/Sorting%20Algos/Merge%20Sort/merge_sort_2.py), can be to modify the given array itself.
In this approach, the space-complexity would be less as compared to the first approach, since we are modifying the array itself, and are not creating any new array.

Broadly,in this particular [implementation of merge sort](https://github.com/noviicee/Search_and_Sort/tree/main/Sorting%20Algos/Merge%20Sort), the *merge()* function is used for merging two halves, and the key function, i.e, *merge_sort()* is used to basically follow the *divide* algorithm of the *divide and conquer*.


**Details-**

Inventor: John von Neumann [Know This Person](https://en.wikipedia.org/wiki/John_von_Neumann)

Worst complexity: n'\*'log(n)

Average complexity: n'\*'log(n)

Best complexity: n'\*'log(n)

Space complexity: n

Stable: Yes [Stable Algorithm](https://en.wikipedia.org/wiki/Stable_algorithm)

#Note: here **n** is considered as the size of the given array
