from heapq import heappush, heappop


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left_child = left

    def set_right_child(self, right):
        self.right_child = right

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __lt__(self, other):
        return (self.value < other.value)


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def traverse_tree(node):
    
    pass


n1 = Node(1)
print("node1 {}".format(n1))

n2 = Node(2)

n3 = Node(3)

n4 = Node(4)

n5 = Node(5)


h = []

heappush(h, n1)

heappush(h, n2)

heappush(h, n3)

heappush(h, n5)

heappush(h, n4)




print("length of h is {}".format(len(h)))
# print len(h)

ordered = []
while h:
    popped = heappop(h)
    print("popped {}".format(popped.value))
    ordered.append(popped)

print("after popping, length of h is {}".format(len(h)))

node16 = Node(16)
heappush(h, node16)
for i in range(len(ordered)):
    item = ordered.pop()
    print("put back {}".format(item.value))

    heappush(h, item)

## take 2 nodes off heap and make a tree

print("initial heap size is {}".format(len(h)))

while len(h) > 1:
    tree = Node(0)    
    pop1 = heappop(h)
    pop2 = heappop(h)
    print("popping {} and {}".format(pop1, pop2))
    print("just popped 2 items and heap len is {}".format(len(h)))
    tree.left_child = pop1
    tree.right_child = pop2
    tree.set_value(pop1.get_value() + pop2.get_value())
    print("new node is {}".format(tree))

    heappush(h, tree)
    print("just pushed 1 tree item and heap len is {}".format(len(h)))


print("size of h is now: {}".format(len(h)))

top = heappop(h)    
print ("top node is {}".format(top.get_value()))    
# if pop1 is not None and pop2 is not None:
#     tree.left_child = pop1
#     tree.right_child = pop2
#     tree.value = pop1.value + pop2.value
#     print("new value is {}".format(pop1.value + pop2.value))

# heappush(h, tree)



ordered = []
while h:
    ordered.append(heappop(h))


for o in ordered:
    print(o.value)