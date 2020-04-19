import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, prev_hash):

      if len(data) == 0:
          data = "NO DATA PROVIDED"

      if not isinstance(timestamp, datetime):
          self.timestamp = datetime.now()

      self.data = data
      self.previous_hash = prev_hash
      self.timestamp = timestamp    
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

    def get_hash(self):
          return self.hash

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        curr = self.head
        s = "--start of chain--\n"
        while curr:
            s += "data: {}\ntimestamp: {}\nhash: {}\nprev hash:{}\n--end of block--\n".format(
                                            curr.data, curr.timestamp, curr.hash, curr.previous_hash)
            if curr.next is None:
                s += "---end of chain---\n"
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

    def get_latest_block(self):
        return self.tail


class Blockchain:

    def __init__(self):
        self.blockchain = LinkedList()

    def pr(self):
        print(self.blockchain)

    def create_genesis_block(self):
        ts = datetime.now()
        new_block = Block(ts, "genesis", "0")
        self.blockchain.append(new_block)


    def add_block(self, new_block):
        if new_block.data == "NO DATA PROVIDED":
            return                       # do not add blocks with no data
        new_block.previous_hash = self.blockchain.get_latest_hash()
        new_block.hash = new_block.calc_hash()
        self.blockchain.append(new_block)

    def get_latest_block(self):
        return self.blockchain.get_latest_block()


bc = Blockchain()
bc.create_genesis_block()                # very first block: the prev hash is set to 0

ts = datetime.now()
new_block = Block(ts, "hello", bc.get_latest_block().get_hash())      # previous hash should look like the genesis block's hash
bc.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "hola", bc.get_latest_block().get_hash())       # previous hash should look like hello's hash
bc.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "gutentag", bc.get_latest_block().get_hash())   # previous hash should look like hola's hash
bc.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "konichiwa", bc.get_latest_block().get_hash())  # previous has should look like gutentag's hash
bc.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "", bc.get_latest_block().get_hash())           # no data provided: do not add to chain
bc.add_block(new_block)

ts = ""                                  # invalid timestamp
new_block = Block(ts, "nihao", bc.get_latest_block().get_hash())
bc.add_block(new_block)

bc.pr()                                  # print all blocks
