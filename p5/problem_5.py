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
        self.create_genesis_block()

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


# Test Case 1: create a blockchain with greetings data and print it out
print("Test Case 1")
bc1 = Blockchain()
# bc.create_genesis_block()                # moved to run whenever a new Blockchain is created

ts = datetime.now()
new_block = Block(ts, "hello", bc1.get_latest_block().get_hash())      # previous hash should look like the genesis block's hash
bc1.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "hola", bc1.get_latest_block().get_hash())       # previous hash should look like hello's hash
bc1.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "gutentag", bc1.get_latest_block().get_hash())   # previous hash should look like hola's hash
bc1.add_block(new_block)

ts = datetime.now()
new_block = Block(ts, "konichiwa", bc1.get_latest_block().get_hash())  # previous has should look like gutentag's hash
bc1.add_block(new_block)



bc1.pr()                                  # print all blocks in Blockchain bc1

print("Test Case 2")

# Test Case 2: create an empty blockchain and print it out. Only the genesis record is there.

bc2 = Blockchain()

bc2.pr()                                  # print all blocks in Blockchain bc2


# Test Case 3: create a blockchain and attempt to add blocks with invalid data. The 2nd and 3rd blocks are successfully added.

print("Test Case 3")
bc3 = Blockchain()

ts = datetime.now()
new_block = Block(ts, "", bc3.get_latest_block().get_hash())                    # no data provided: do not add to chain
bc3.add_block(new_block)                

ts = ""                                                                         # no timestamp provided
new_block = Block(ts, "whatdayisit", bc3.get_latest_block().get_hash())
bc3.add_block(new_block)  

ts = datetime.now()                                                              # acceptably defined block
new_block = Block(ts, "igetit", bc3.get_latest_block().get_hash())
bc3.add_block(new_block)  

bc3.pr()             # both the 2nd and 3rd blocks (timestamp added when missing) were added but not the one with no data
