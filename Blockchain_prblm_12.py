# Write a Python program to Demonstrate a Simple Implementation of a Blockchain Using Hash Codes as a Chain of Blocks

import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the SHA-256 hash of the block's content.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the first block in the blockchain.
        """
        return Block(0, time(), "Genesis Block", "0")

    def add_block(self, data):
        """
        Add a new block to the blockchain.
        """
        previous_block = self.chain[-1]
        new_block = Block(
            previous_block.index + 1, time(), data, previous_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Check the validity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate the current block's hash and verify it matches
            if current_block.hash != current_block.calculate_hash():
                print(f"Hash mismatch at Block {current_block.index}")
                return False

            # Verify the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous hash mismatch at Block {current_block.index}")
                return False

        return True

# Test the blockchain
blockchain = Blockchain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

print("Blockchain is valid:", blockchain.is_chain_valid())

# Tamper with the data of a block
blockchain.chain[1].data = "Tampered Transaction"

# Recalculate the hash after tampering
blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()

print("Blockchain is valid after tampering:", blockchain.is_chain_valid())
