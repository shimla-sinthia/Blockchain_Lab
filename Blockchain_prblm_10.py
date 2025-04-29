#Write a program in Python that Demonstrates How to Use the SHA-256 Hash Function and Its Application in a Simple Blockchain

import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine block attributes and hash them using SHA-256
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block in the blockchain
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        # Add a new block to the blockchain
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, previous_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        # Display all blocks in the blockchain
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 70)

# Demonstrate the blockchain
print("=== Simple Blockchain Using SHA-256 ===\n")

# Create a blockchain
my_blockchain = Blockchain()

# Add new blocks
my_blockchain.add_block("First Transaction")
my_blockchain.add_block("Second Transaction")
my_blockchain.add_block("Third Transaction")

# Display the blockchain
my_blockchain.display_chain()
