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
        heappush(heap, node)
        # print("pushing node of value {}".format(k))

    # create mini-trees with two lowest frequency values and merge trees
    #   until all nodes are under one parent
    while len(heap) > 1:
        tree = Node(0)    
        pop1 = heappop(heap)
        pop2 = heappop(heap)
        tree.left_child = pop1
        tree.right_child = pop2
        tree.set_value(pop1.get_value() + pop2.get_value())

        heappush(heap, tree)

    top = heappop(heap)    
    return top  # encode/decode tree


encode_table = {}   

def new_encode_table():
    encode_table.clear()


def encode(node, charstr):

    if node:
        # print("encode {} {}".format(charstr, node.get_letter(), node.get_value()))

        if node.get_letter() != '':
            node.set_code(charstr)
            encode_table[node.get_letter()] = node.get_code()

        encode(node.get_left_child(), charstr+'0')

        encode(node.get_right_child(), charstr+'1')

    return encode_table


def huffman_encoding(data):   
    if data == "":
        return "", Node(0)

    top = huffman_build_tree(data)                 # build the encode/decode tree

    if top.get_left_child() == None and top.get_right_child() == None:   # if only one character in input
        encode_table[top.get_letter()] = str(top.get_value())
    else:
        encode(top, "")                            # traverse tree to create codes

    # print("printing encode_table")
    # for k, v in encode_table.items():
    #     print("{} {}".format(k, v))


    encoded = ""
    for c in data:
        encoded += encode_table[c]

    return encoded, top

def huffman_decoding(str, node):
    # decode the str provided using provided tree (node)

    if str == "":
        return ""

    if node is None:
        return ""

    curr = node
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

    return res

# Test Case 1 

new_encode_table()

str_to_encode = "oh hello i am a nice happy string yes indeed"
print ("The size of the data is: {}\n".format(sys.getsizeof(str_to_encode)))
print ("The content of the data is: {}\n".format(str_to_encode))

encoded_data, tree = huffman_encoding(str_to_encode)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))
        


# Test Case 2

new_encode_table()
str_to_encode = "it is a very nice day don't mind the clouds"
print ("The size of the data is: {}\n".format(sys.getsizeof(str_to_encode)))
print ("The content of the data is: {}\n".format(str_to_encode))

encoded_data, tree = huffman_encoding(str_to_encode)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))        



# Test Case 3

new_encode_table()
str_to_encode = "a"
print ("The size of the data is: {}\n".format(sys.getsizeof(str_to_encode)))
print ("The content of the data is: {}\n".format(str_to_encode))

encoded_data, tree = huffman_encoding(str_to_encode)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))   


# Test Case 4

new_encode_table()
str_to_encode = "ah"
print ("The size of the data is: {}\n".format(sys.getsizeof(str_to_encode)))
print ("The content of the data is: {}\n".format(str_to_encode))

encoded_data, tree = huffman_encoding(str_to_encode)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))   


# Test Case 5: empty string

new_encode_table()
str_to_encode = ""

print ("The size of the data is: {}\n".format(sys.getsizeof(str_to_encode)))
print ("The content of the data is: {}\n".format(str_to_encode))

encoded_data, tree = huffman_encoding(str_to_encode)

print ("The size of the encoded data is: {}\n".format(0))  # have to hard-code this because cannot do int() operation on blank string
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(0))  # same here: the size of a blank string is actually not zero
print ("The content of the decoded data is: {}\n".format(decoded_data))   
