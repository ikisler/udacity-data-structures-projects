import hashlib, datetime

class Block:
    def __init__(self, timestamp, data, previous_hash = None, previous = None):
        self.timestamp = timestamp
        self.data = str(data or "") # Catch edge case when data is None -- convert to empty string
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = previous

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        return """
            Data: {}
            Timestamp: {}
            Hash: {}
            Previous Hash: {}""".format(self.data, str(self.timestamp), self.hash, self.previous_hash)

class BlockChain:
    def __init__(self):
        self._tail = None # Tail in this case is the newest block of our chain
        self._count = 0

    def add_block(self, data):
        self._count += 1
        if self._tail is None:
            # Genesis block does not have a previous hash or block to link to
            self._tail = Block(datetime.datetime.utcnow(), data)
            return
        new_block = Block(datetime.datetime.utcnow(), data, self._tail.hash, self._tail)
        self._tail = new_block

    def get_count(self):
        return self._count

    def __repr__(self):
        current = self._tail
        out = "Block count: " + str(self.get_count()) + "\n\nBlocks:"
        if self.get_count() == 0:
            return out + "\nNone"
        while current:
            out += "\n" + str(current)
            current = current.previous
        return out

# Test general case of adding blocks with data
chain = BlockChain()
chain.add_block("Data one")
chain.add_block("Data Two")
chain.add_block("Data Three")

print(chain)
# Should return a printout showing count of 3 block and details of each, including data and hashes

print("--------------------------------------------")

# Test edge case where block data is empty string or None type
chain = BlockChain()
chain.add_block("")
chain.add_block(None)

print(chain)
# Should return a printout showing count of 3 block and details of each, including empty data for both blocks

print("--------------------------------------------")

# Test when no blocks are added
chain = BlockChain()
print(chain)
# Should return printout showing block count of 0, and no blocks in the list

