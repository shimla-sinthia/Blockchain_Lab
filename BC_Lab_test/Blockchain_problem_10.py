#Task 10: Write a program in Python that Demonstrates How to Use the SHA-256 Hash Function and Its Application in a Simple Blockchain

import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Initializes a block with index, timestamp, data, and previous hash.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()  # Compute the hash at creation

    def calculate_hash(self):
        """
        Calculates SHA-256 hash of the block using its attributes.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()

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
        return Block(0, time(), "Genesis Block", "0")

    def add_block(self, data):
        """
        Mines and adds a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, time(), data, previous_block.hash)

        # Recalculate hash after setting previous_hash
        new_block.hash = new_block.calculate_hash()
        
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hashes and previous hash links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate hash and compare with stored hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has an invalid hash.")
                return False

            # Check if previous_hash value matches actual previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} has an invalid previous hash.")
                return False

        return True

# === Running the Blockchain ===
blockchain = Blockchain()

# Adding blocks with transaction data
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

# Check if the blockchain is valid
print("Blockchain is valid:", blockchain.is_chain_valid())

# Tampering with the second block
blockchain.chain[1].data = "Tampered Transaction"

# Revalidate the blockchain after tampering
print("Blockchain is valid after tampering:", blockchain.is_chain_valid())
