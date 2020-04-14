from heapq import heappush, heappop

heap = []
# data = [1, 4, 2, 6, 9, 3]

# for item in data:
#     heappush(heap, item)


# ordered = []
# while heap:
#     ordered.append(heappop(heap))


# print(ordered)

class Node(object):
    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq
        self.left = None
        self.right = None




dict = {}
def count_letters(str):
    for a in str:
        dict[a] = dict.get(a, 0) + 1

    for k, v in dict.items():
        print(v, k)
        heappush(heap, (v, k))

    ordered = []
    while heap:
        ordered.append(heappop(heap))

    print(ordered)

count_letters("hello lllh")