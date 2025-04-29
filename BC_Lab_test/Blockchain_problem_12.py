# Task 12: Write a Python program to Demonstrate a Simple Implementation of a Blockchain Using Hash Codes as a Chain of Blocks

import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        """
        Initializes a new block with a timestamp, data, and previous block hash.
        """
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Generates a SHA-256 hash of the block's contents.
        """
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Initializes the blockchain with a Genesis Block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block of the blockchain (Genesis Block).
        """
        return Block(datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Returns the most recently added block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain.
        """
        new_block.previous_hash = self.get_latest_block().hash  # Link the new block
        new_block.hash = new_block.calculate_hash()  # Recalculate hash
        self.chain.append(new_block)

    def is_valid(self):
        """
        Validates the blockchain by checking hashes and previous hash links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous_hash matches the actual previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# === Creating the Blockchain ===
blockchain = Blockchain()

# Adding new blocks with data
blockchain.add_block(Block(datetime.datetime.now(), "Block 1", ""))
blockchain.add_block(Block(datetime.datetime.now(), "Block 2", ""))
blockchain.add_block(Block(datetime.datetime.now(), "Block 3", ""))

# Check if the blockchain is valid
print("Is blockchain valid?", blockchain.is_valid())

# === Tampering with the blockchain ===
blockchain.chain[1].data = "Modified Block"

# Check blockchain validity after tampering
print("Is manipulated blockchain valid?", blockchain.is_valid())
