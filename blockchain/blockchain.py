import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, prev_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = prev_hash
      self.hash = self.calc_hash()
      self.next = None
      self.prev = None

    def __str__(self):
        s = " timestamp: {}\ndata: {}\nhash: {}\nprevious hash: {}\n".format(self.timestamp,
                                                self.data, self.hash, self.previous_hash)
        return s

    def calc_hash(self):
          sha = hashlib.sha256()

          hash_str = (str(self.timestamp) + self.data + self.previous_hash).encode('utf-8')
          # hash_str = "We are going to encode this string of data!".encode('utf-8')

          sha.update(hash_str)

          return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        curr = self.head
        s = ""
        while curr:
            s += " {}: {}->".format(curr.data, curr.hash)
            curr = curr.next

        return s

    def append(self, node):
        ts = datetime.now()
        if self.head is None:
            self.head = node
            self.tail = self.head
            return


        prev_hash = self.tail.previous_hash
        self.tail.next = node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def get_latest_hash(self):
        return self.tail.hash


class Blockchain:

    def __init__(self):
        self.blockchain = LinkedList()

    def create_genesis_block(self):
        ts = datetime.now()
        new_block = Block(ts, "genesis", "0")
        self.blockchain.append(new_block)
        print(self.blockchain)


    def add_block(self, new_block):
        new_block.previous_hash = self.blockchain.get_latest_hash()
        new_block.hash = new_block.calc_hash()
        self.blockchain.append(new_block)
        print(self.blockchain)



bc = Blockchain()
bc.create_genesis_block()    # very first block

ts = datetime.now()
new_block = Block(ts, "hello", "1")
bc.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "hola", "2")
bc.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "gutentag", "3")
bc.add_block(new_block)

