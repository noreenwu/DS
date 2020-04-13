import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, prev_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = prev_hash
      self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)
      self.next = None
      self.prev = None

    def calc_hash(self, ts, data, prev_hash):
          sha = hashlib.sha256()

          hash_str = (str(ts) + data + prev_hash).encode('utf-8')
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
            s += " {}->".format(curr.data)
            curr = curr.next

        return s

    def append(self, value):
        ts = datetime.now()
        if self.head is None:
            self.head = Block(ts, value, "0000")
            self.tail = self.head
            return


        prev_hash = self.tail.previous_hash
        self.tail.next = Block(ts, value, prev_hash)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def get_latest(self):
        return self.tail


class Blockchain:

    def __init__(self):
        self.blockchain = LinkedList()

    def create_genesis_block(self):
        self.blockchain.append("genesis")
        print(self.blockchain)

    def get_latest_block(self):
        return self.blockchain.get_latest()

    def add_block(self, new_block):
        new_block.previous_hash = get_latest_block().hash
        new_block.hash = new_block.calc_hash()



bc = Blockchain()

bc.create_genesis_block()

