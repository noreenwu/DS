# LRU Cache
In a Least Recently Used Cache, items that are frequently used are kept on hand (easily accessible).
Specifically, the least recently used items will be removed from the cache as space runs out. The whole
point of caching is quick access, so all operations--set, get, is there a hit--need to take place quickly.
Whenever an item is updated or accessed, it is considered "used" and is moved to the back of the queue.

## Time Efficiency: 

The cache is implemented with a hash and a linked list. The hash allows O(1) retrieval
and access to an item, and the linked list allows O(1) expiration of the LRU item. New items are added to the
hash and to the tail of the list. Items being expired from the cache when at capacity are removed from
the front (head) of the list. If an item is accessed or updated, the update takes place in O(1) time
and the moving of the item to the end of the LRU linked list takes O(1).

The capacity of the cache is set when it is created.

The number of entries is incremented whenever something is put into the cache. 


## Space Efficiency:

The space requirements for the cache are a function of the size of the objects being stored. 
All operations are done in place, so once the space is allocated for the cache, the
space requirements do not change.

