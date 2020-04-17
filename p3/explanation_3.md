# Huffman Coding

Huffman Coding is a lossless compression technique that determines the encoding patterns based on each
character's frequency in the data set. Characters that show up frequently are given shorter codes than
the infrequent ones, optimizing the compression. 

To Huffman encode a string or data set, first the frequency of characters needs to be determined.
Using this frequency data, a Node for each character is created and pushed on to a priority queue
(heapq). Each of these Nodes may be thought of as a tree that will become part of a single tree. 

The lowest two frequency nodes are popped off the priority queue and assigned as children of a new node whose 
value is the sum of the frequencies of each of its children. This new node (parent of tree) is pushed on to the
priority queue; its value may shift its placement on the queue, depending on the other node values. This process
of popping 2 children and pushing back a new parent of these children continues until there is a single tree with
nodes, with the nodes containing characters at the leaves. In the final tree, characters that appear less frequently
in the data are pushed to deeper levels, which correspond to longer encoding keys compared to the shallower leaf nodes.

For convenience in the actual encoding process, the codes determined from building this tree are put into a hash. 
To do this, the tree is traversed, depth-first, recursively, and whenever a leaf node, containing a character is encountered,
its value and the left-right steps that were needed to reach it are saved as that letter's code in the hash.

## Time Complexity

Determine frequency of characters: O(N)

Create nodes and push these on to priority queue (heapq), based on character's frequency: O(N)

Combine nodes into a single encoding tree. O(N)

Capture codes into hash table by traversing tree.  O(N + M), where N is the number of nodes and M
is the number of edges.  N in practice will be no more than twice the original number of unique characters.
M will also be, worst case, on the order of 2 x the number of original nodes.

Encode by walking through data one char at a time and using the code saved for the character (in the hash)
to build the encoded data. O(N)

The entire encoding process ends up being a multiple of O(N) -- even though there are a number of steps,
each of them is on the order of O(N).





## Space Complexity

