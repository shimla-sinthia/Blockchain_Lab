# Task 6: Implementing Proof of Work (PoW) Algorithm

import hashlib
import time


class PoWBlock:
    def __init__(self, index, previous_hash, timestamp, data, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.mine_block()

    def calculate_hash(self):
        """Calculates the hash for the block by including the nonce."""
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        """Performs the Proof of Work by finding a hash with the required difficulty."""
        prefix = "0" * self.difficulty
        while True:
            hash_candidate = self.calculate_hash()
            if hash_candidate.startswith(prefix):
                return hash_candidate
            self.nonce += 1

class PoWBlockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Creates the first block in the blockchain."""
        genesis_block = PoWBlock(0, "0", time.time(), "Genesis Block", self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        """Adds a new block to the blockchain after mining it."""
        latest_block = self.get_latest_block()
        new_block = PoWBlock(len(self.chain), latest_block.hash, time.time(), data, self.difficulty)
        self.chain.append(new_block)

# Example usage
blockchain = PoWBlockchain(difficulty=3)
blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")

# Display the blockchain
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Nonce: {block.nonce}")
    print("-" * 70)
