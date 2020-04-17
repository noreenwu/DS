from heapq import heappush, heappop
import sys

class Node(object):
    def __init__(self, value, letter=''):
        self.letter = letter
        self.value = value
        self.left_child = None
        self.right_child = None
        self.code = ""

    def get_letter(self):
        return self.letter

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

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

def huffman_build_tree(data):
    # count frequency of letters
    dict = {}    
    for a in data:
        dict[a] = dict.get(a, 0) + 1

    # create priority queue of nodes, using frequency data collected
    heap = []
    for k, v in dict.items():
        node = Node(v, k)
        print ("new node {}".format(node))
        heappush(heap, node)

    # create mini-trees with two lowest frequency values and merge trees
    #   until all nodes are under one parent
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

    return top  # encode/decode tree


encode_table = {}   

def encode(node, charstr):
    visit_order = []    
  
    if node:
        if node.get_letter() != '':
            visit_order.append(node.get_value())
            node.set_code(charstr)
            print("letter {} assigned {}".format(node.get_letter(), node.get_code()))
            encode_table[node.get_letter()] = node.get_code()

        encode(node.get_left_child(), charstr+'0')

        encode(node.get_right_child(), charstr+'1')

    return encode_table


def huffman_encode(data, tree):
    ## traverse tree and create codes
    print("huffman_encode")
   
    encode(top, "")

    print("Encoding table: ")
    for k, v in encode_table.items():
        print("k {}: {}".format(k, v))


    encoded = ""
    for c in data:
        print(c)
        encoded += encode_table[c]

    return encoded

def huffman_decode(str, node):
# def decode(str, node):
    if node is None:
        return
    curr = node
    print ("decode {}".format(node.get_value()))
    res = ''    
    for s in str:
        if s == '0':
            if (curr.has_left_child()):
                curr = curr.get_left_child()
        elif s == '1':
            if (curr.has_right_child()):
                curr = curr.get_right_child()

        if curr.get_letter() != '':
            res += curr.get_letter()
            curr = node

    print (res)
    return res


str_to_encode = "helllotherelongstring"
print ("The size of the data is: {}\n".format(sys.getsizeof(str_to_encode)))
print ("The content of the data is: {}\n".format(str_to_encode))

top = huffman_build_tree(str_to_encode)

encoded = huffman_encode(str_to_encode, top)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded))

# print(encoded)

decoded = huffman_decode(encoded, top)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded)))
print ("The content of the encoded data is: {}\n".format(decoded))
        