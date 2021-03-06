

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.lru_head = None
        self.lru_tail = None
        self.cache = {}
        self.max_values = capacity
        self.num_entries = 0


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cache.get(key, -1) == -1:
            return -1


        retval = self.cache[key].value
        self.LRU_update(self.cache[key], key, self.cache[key].value)
        return retval



    def LRU_append(self, new_node):
        if self.lru_head is None:
            self.lru_head = new_node
            self.lru_tail = new_node
            new_node.prev = None

        else:
            new_node.prev = self.lru_tail
            self.lru_tail.next = new_node
            self.lru_tail = new_node

    def LRU_update(self, node, key, value):
        if self.lru_head == node:
            # if node was first in list
            self.lru_head = self.lru_head.next

        elif self.lru_tail == node:
            return

        else:
            # remove the specified node by making its predecessor skip over specified node
            node.prev.next = node.next

        # node.prev = self.lru_tail
        n = Node(key, value)   # for some reason, cannot point to old node at end of list so made new node w/ same value
        # n = self.cache[key]

        self.lru_tail.next = n
        n.prev = self.lru_tail
        self.lru_tail = n
        self.cache[key] = n


    def LRU_remove_oldest(self):
        if self.lru_head is None:
            return

        del(self.cache[self.lru_head.key])

        if self.lru_head == self.lru_tail:   # one item in list
            self.lru_tail = self.lru_tail.next

        self.lru_head = self.lru_head.next


    def set(self, key, value):

        # if the key is present in the cache
        if key in self.cache:
            # reset the value and update the LRU order
            self.LRU_update(self.cache[key], key, value)
            return

        # else, if new value, check if there is room in the cache

        # if cache is full
        if self.num_entries >= self.max_values:
            ## remove oldest
            self.LRU_remove_oldest()
            self.num_entries -= 1

        # now create new item
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.LRU_append(new_node)   # add (point to) new item to end of list
        self.num_entries += 1


    def __repr__(self):
        curr = self.lru_head

        str = "cache has {} entries:\n\t".format(self.num_entries)

        while curr:
            num = curr.value
            str += "node {}, ".format(curr.value)
            curr = curr.next
        str += "\n"
        return (str)


# Test Case 1: Create a Cache. Before setting any values, what gets returned?
print("Test Case 1: Retrieve a value when nothing in cache (get -1)")
our_cache = LRU_Cache(5)
print("get 10 : ", our_cache.get(10))        # return -1


# Test Case 2: Put some values into the cache: should be able to retrieve the set values. 
#   once a value is retrieved, that item should move to the end of the line as it was
#   the most recently used.
print("\nTest Case 2: Put some values into the cache, check that they are in the right order")
print("set 1, 2, 3, 4")
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache)

print("\nTest Case 3: Retrieve values from the cache. They should rotate to end of list when accessed")
print("get 1 : ", our_cache.get(1))         # returns 1

print(our_cache)

print("get 2 : ", our_cache.get(2))         # returns 2

print(our_cache)


# Test Case 3: Retrieve something that was never put into the cache
print("\nTest Case 4: Now check something that was never put into the cache (get -1)")

print("get 9 (expect -1): {}\n".format(our_cache.get(9)))     # returns -1 (9 is not in the cache)

# Test Case 4: Put some more data into the cache. Now we have exceeded the size of the cache, so the
#   least recently used item needs to be bumped out. In this case, that value is 3.
print("set 5, 6")
our_cache.set(5, 5)

our_cache.set(6, 6)

print(our_cache)

print("get 3 (was LRU and bumped, expect -1): {}\n".format(our_cache.get(3)))     # returns -1 (3 was bumped off cache because LRU)


# Test Case 5: Put something else into the cache, value 7. Node 4 gets bumped out
print("set 7")
our_cache.set(7, 7)

print(our_cache)