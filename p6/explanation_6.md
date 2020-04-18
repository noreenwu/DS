# Union and Intersection of Two Linked Lists

Given 2 linked lists, specified by arrays of elements and created by appending each item to the list,
return the union or the intersection of the linked lists. Neither result will include duplicates,
even if the original arrays did. 

The use of hashes easily eliminates any duplicates in the first list. To find the union, add any 
unseen values to the dictionary and while checking, also add any new values to a new linked list. 
Continue adding unseen values while looping through the second list.

To find the intersection, begin also by building a dictionary of values seen in the first list. 
Then, while looping through the second list, only append those values that appear in both lists
to the final result.


## Time and Space Analysis

In both cases, finding the union and intersection involves looping through both linked lists.
However, thanks to hashes, it is possible to find either the union or the intersection on
the first pass. Therefore the running time of both of these algorithms is O(N), where N is the
total number of nodes in both lists.

For space, other than the space occupied by the lists in the first place, space is required
for the hashes at a worst case size of O(N), with N being the total number of values in
both arrays, plus O(N) space for the new linked list being returned.




