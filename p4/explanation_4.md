# Active Directory

In Windows Active Directory, a group may include both users and other groups. The method
user_in_group may be called repeatedly (on each group within a group) to determine whether a user 
is in the group or in one of its subgroups (or sub-subgroups, etc). 

If a user is found in a group, however deeply nested, the method returns True and that call is 
removed from the stack, allowing its caller to return True, until the first instance of the method call
returns True. If user_in_group returns False, nothing has been determined and the top
level loop to check all groups continues. 

## Time Complexity

The worst case for this is if the user is in the very last group checked, or if the user is not in
any of the nested groups, which is O(N), where N is the number of groups that have to be checked.


## Space Complexity

No additional space for this algorithm is needed. 

