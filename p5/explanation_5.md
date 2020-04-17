# Blockchain

A blockchain is a sequential chain of records, which could represent transactions,
that is stored in multiple places across a network. Each record contains its data,
a timestamp indicating when it was created, the previous block's hash, and the block's own hash, 
which is dependent on the block's data and on the previous block's hash. This makes it
impossible to change the data in a block, because that would require a recompute of 
its hash, which would invalidate all subsequent blocks.


## Time Space Analysis

The blockchain is implemented as a Linked List, with a pointer to the head of the list
and to the tail of the list. So adding a new Block can be done in O(1). This implementation
of Blockchain does not make it easy to find a specific Block. The current implementation
would require O(N) steps to look through the entire Linked List for a matching record.

The space requirements are a Block for each transaction, or O(N).
