# Finding Files (Recursive)

This function recursively looks through directories starting with the one specified, and
prints out all files ending in .c. After obtaining a listing of the current directory, 
it checks if any of these items is a directory itself. If so, it looks through that directory
and does the same. The base case is not explicitly specified with a return statement,
but the function does not call itself unless it encounters a directory.  If a file ends
in .c, it is printed.


## Time and Space Efficiency

No data structures or storage are required for this exercise, so the space taken is just
whatever space is taken by the size of the directory structure specified.

The time complexity is dependent on the number of files that exist in the structure. 
If there are N files, each is checked; if one of those is a directory, then each file
in that directory is checked, so although this is a recursive implementation, the 
time complexity is still O(N), where N is the total number of files.



