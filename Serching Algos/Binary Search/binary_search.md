Binary Search Algorithm in Python.
----------------------------------

->The Binary Search is a searching algorithm in python, which searches for an empty element in a given array/list, and returns the index of the position where the element was found.


->Unlike linear search, the Binary Search algorithm works by repeatedly dividing in half the portion of the list that could contain the item, until the list's possible locations is narrowed down to just one.

->It works on the principle of "divide and conquer'.

->The only requirement is that the given list must be sorted.


Space-Time Complexity of Binary Search.
--------------------------------------
--------------------------------------


->Time-Complexity of Binary Search= O(logN) ; N=size of the array (since in each iteration(in iterative approach) or in each recursive call(as in here), the search gets reduced to half of the array.)

#This is the Worst-Case Time-Complexity

->>This can happen if the required element is found at the last position of the  array when it's narrowed down to a single item.


->Space-Complexity of Binary Search
-----------------------------------

->The space-complexity of Binary Search depends on the type of method one is using to implement the algorithm.

->>One can basically use two methods to implement the Binary Search Algorithm-

1). Iterative Method #links to be added 

2). Recursive Method [recursive implementation of binary search](https://github.com/noviicee/Search_and_Sort/blob/main/Serching%20Algos/Binary%20Search/binary_search_recursive.py) 


Therefore, the Auxilliary Space-Complexity of the Binary-Search can be given as-

->Iterative method: O(1)

->Recursive method: O(log(N)) ; N=size of the array


Advantage of using Binary Search Algorithm.
------------------------------------------


->It eliminates half of the list from further searching by using the result of each comparison.

->The time complexity of binary search remains unchanged irrespective of the element position even if it is not present in the array.

->For large lists of data, it works significantly better than linear search.


Disadvantages of using the Binary Search Algorithm.
--------------------------------------------------


->The given array/list MUST be sorted.

->The recursive approach of Binary Search requires more stack space.

->The interaction of binary search with memory hierarchy i.e. caching is poor. (because of its random access nature)
