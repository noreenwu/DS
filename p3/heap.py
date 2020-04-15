from heapq import heappush, heappop


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        else:
            return 0


n1 = Node(1)

n2 = Node(2)

n3 = Node(5)

h = []

heappush(h, n1)

heappush(h, n2)

heappush(h, n3)

ordered = []
while h:
    ordered.append(heappop(h))