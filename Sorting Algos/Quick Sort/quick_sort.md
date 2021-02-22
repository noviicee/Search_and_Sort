Quick Sort
-----------
-----------

The quick sort is a sorting technique and is often used, right alongside Merge Sort.

[**The basic version of the algorithm**](#) does the following:

->Divide the collection in two (roughly) equal parts by taking a pseudo-random element and using it as a pivot.

->Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it.

->This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

#Note that:
When we describe elements as "larger" or "smaller" than another element - it doesn't necessarily mean larger or smaller integers, we can sort by any property we choose.

For an example-If we have a custom class Person, and each person has a name and age, we can sort by name (lexicographically) or by age (ascending or descending).

The problem with this basic approach is that we atually don't know how many times we will need to form the left and the right subarray. Since this follows a recursive approach, the Time-Complexity can prove to be really costly, not to forget the space-complexity too, because we are creating new arrays repeteadly.

To mention the estimates more clearly-


If time-complexity of quick_sort_basic [code](#) is taken as T(n), then-

n(log(n))<=T(n)<=n^2


T(n) will be equal to n(log(n)) only when the pivot is actually the *middle item in the final sorted array*


Not to forget the the Space-Complexity is going to be very high due to the repetitive creation of the left and right subarrays.


Hence, this appproch is better for understanding the step-by-step implementation of how actually the quick-sort algorithm works.


The general approach, i.e, the approach, which is most commonly used is-

General Logic of Quick-Sort
------------------------------
------------------------------


