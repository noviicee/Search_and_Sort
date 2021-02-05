Linear Search Algorithm in Python.
----------------------------------


->The Linear Search is a searching algorithm in python, which searches for an empty element in a given array/list, and returns the index of the position where the element was found.


->Linear Search is also known as 'Brute-Force' search.

->>Usually “brute-force” is a term reserved for exploring search spaces that are of exponential size, but we can use it here too.


In Linear Search, we check ALL possible positions and if the item is found, we return the match.

If not, we report that it is not found, but we can conclude this only after checking all the entries in the given array.


As the strategy is that we check all positions, we can say this is a brute-force approach.

->>>It’s an effective brute-force approach, since the space is only linear in size with respect to the input size.


Space-Time Complexity of Linear Search.
--------------------------------------


->Time-Complexity of Linear Search= O(N) ; N=size of the array #Worst-Case Time-Complexity (if the required element is found at the last position of the  array, or the element is not presebt in the given array.)

->>This is obvious since we are traversing all the elements one-by-one, without jumping in order to find our required element.


->Space-Complexity of Linear Search= O(1) ; constant space-complexity

->>This is because we are not using any extra space, we are just checking for the given element sequentially in the given array itself. Henec, the space complexity will always be constant.


Advantage of using Linear Search Algorithm.
------------------------------------------


->One advantage of Linear Searching is that we don't require a sorted array.

->>We won’t be able to do much better with an unordered array as you have no idea where the item you are searching for is located in the worst case.

->Linear Search will perform fast searches of small to medium lists.

->It remains unaffected by insertions and deletions.

->>As the linear search does not require the list to be sorted, additional elements can be added and deleted.

->>>As other searching algorithms may have to reorder the list after insertions or deletions, this may sometimes mean a linear search will be more efficient.



Disadvantages of using the Linear Search Algorithm.
--------------------------------------------------


->In the case of large lists, Linear Search may prove to be really slow.

->>For example, when searching through a database of everyone in the Northern Ireland to find a particular name, it might be necessary to search through 1.8 million names before you found the one you wanted.


------------------------------------------------------------------------------------
This speed disadvantage is the reason why other search methods have been developed.
-------------------------------------------------------------------------------------
