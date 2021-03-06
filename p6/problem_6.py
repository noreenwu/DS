class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        if out_string == "":
            return "no elements"
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size



def union(llist_1, llist_2):
    # loop thru each list and check a hash to see if item was seen before.
    # only add it to final list if not seen before. add each unseen item to hash.

    new_llist = LinkedList()
    dict = {}

    curr = llist_1.head
    while curr:
        if dict.get(curr.value) is None:
            # add to new linked list
            # add to dict
            dict[curr.value] = 1
            new_llist.append(curr.value)
        curr = curr.next

    curr = llist_2.head
    while curr:
        if dict.get(curr.value) is None:
            dict[curr.value] = 1
            new_llist.append(curr.value)
        curr = curr.next


    return(new_llist)


def intersection(llist_1, llist_2):

    new_llist = LinkedList()
    dict = {}

    curr = llist_1.head
    while curr:
        if dict.get(curr.value) is None:
            dict[curr.value] = 1

        curr = curr.next

    curr = llist_2.head
    while curr:
        if dict.get(curr.value) != None:
            # add to new linked list
            new_llist.append(curr.value)

        curr = curr.next

    return (new_llist)

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("lists 1 and 2")
# print(linked_list_1)
# print(linked_list_2)
print ("union :", union(linked_list_1,linked_list_2))                  # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print ("intersection : ", intersection(linked_list_1,linked_list_2))   # 6 -> 4 -> 6 -> 21 -> 

# # Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("\nlists 3 and 4")
# print(linked_list_3)
# print(linked_list_4)
print ("union :", union(linked_list_3,linked_list_4))             #  3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->   
print ("intersection : ", intersection(linked_list_3,linked_list_4))      # no elements


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [2, 3, 6]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("\nlists 5 and 6")
print ("union : ", union(linked_list_5, linked_list_6))                    # 2 -> 3-> 6
print ("intersection : ", intersection(linked_list_5, linked_list_6))      # no elements


# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("\nlists 7 and 8")
print ("union : ", union(linked_list_7, linked_list_8))                    # no elements
print ("intersection : ", intersection(linked_list_7, linked_list_8))      # no elements