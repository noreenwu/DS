from heapq import heappush, heappop

heap = []


class Node(object):
    def __init__(self, value, letter=''):
        self.letter = letter
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
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __lt__(self, other):
        return (self.value < other.value)




dict = {}
def count_letters(str):
    for a in str:
        dict[a] = dict.get(a, 0) + 1

    for k, v in dict.items():
        node = Node(v, k)
        print ("new node {}".format(node))
        heappush(heap, node)

    # ordered = []
    # while heap:
    #     ordered.append(heappop(heap))

    # print(ordered)

count_letters("hellooo")

print("initial heap size is {}".format(len(heap)))

while len(heap) > 1:
    tree = Node(0)    
    pop1 = heappop(heap)
    pop2 = heappop(heap)
    print("popping {} and {}".format(pop1, pop2))
    print("just popped 2 items and heap len is {}".format(len(heap)))
    tree.left_child = pop1
    tree.right_child = pop2
    tree.set_value(pop1.get_value() + pop2.get_value())
    print("new node is {}".format(tree))

    heappush(heap, tree)
    print("just pushed 1 tree item and heap len is {}".format(len(heap)))


print("size of h is now: {}".format(len(heap)))

top = heappop(heap)    
print ("top node is {}".format(top.get_value()))    


## traverse tree and create codes
visit_order = []
def traverse(node):
    if node:
        if node.get_value != '':
            visit_order.append(node.get_value())

        traverse(node.get_left_child())

        traverse(node.get_right_child())

    return visit_order


print(traverse(top))



        