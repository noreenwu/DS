from heapq import heappush, heappop


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # def __cmp__(self, other):
    #     if self.value < other.value:
    #         return -1
    #     elif self.value > other.value:
    #         return 1
    #     else:
    #         return 0

    def __lt__(self, other):
        return (self.value < other.value)

n1 = Node(1)

n3 = Node(5)

n2 = Node(2)

n4 = Node(11)

n5 = Node(0)


if n1 > n3:
    print("n1 bigger")
else:
    print("n5 bigger")
h = []

heappush(h, n1)

heappush(h, n2)

heappush(h, n3)

heappush(h, n4)

heappush(h, n5)

ordered = []
while h:
    ordered.append(heappop(h))

for o in ordered:
    print(o.value)