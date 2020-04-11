

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


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
        pass

    def update_lru(self, key, new_node):
        #  if the key is there already, then update the value and move the node to end
        #    of LRU list

        #  if the key is not there, create it, and append it to node at end
        #  if the cache is maxed out, then delete the LRU item

        pass

    def set_cache_value(self, key, value):

        new_node = Node(value)
        self.cache[key] = new_node
        update_lru(key, new_node)

        self.num_entries += 1

    def remove_oldest(self):
        # find oldest

        # delete it
        pass

    def LRU_append(self, new_node):
        print("LRU_append")
        if self.lru_head is None:
            self.lru_head = new_node
            self.lru_tail = new_node

        else:
            self.lru_tail.next = new_node
            self.lru_tail = new_node
            print("appended and moved the tail")

    def LRU_remove_oldest(self):
        if self.lru_head is None:
            return

        if self.lru_head == self.lru_tail:
            self.lru_tail = self.lru_tail.next

        self.lru_head = self.lru_head.next


    def set(self, key, value):

        # if the key is present in the cache
        if self.cache.get(key) != None:
            # reset the value and update the LRU order
            return

        # else, if new value, check if there is room in the cache

        # if cache is full
        if self.num_entries >= self.max_values:
            ## remove oldest
            print("MAX ENTRIES in cache")
            self.LRU_remove_oldest()

        # now create new item
        new_node = Node(value)
        self.cache[key] = new_node
        self.LRU_append(new_node)   # add (point to) new item to end of list
        self.num_entries += 1


    def __repr__(self):
        curr = self.lru_head

        str = ""
        while curr:
            num = curr.value
            str += "node {}, ".format(curr.value)
            curr = curr.next
        return (str)


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.set(5, 5);
our_cache.set(6, 6);

print(our_cache)

# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5)
# our_cache.set(6, 6)

# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
