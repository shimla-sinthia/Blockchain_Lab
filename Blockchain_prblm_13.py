#Write a Python program to Demonstrate the Mining Process in Blockchain

import hashlib
import time

class MiningBlock:
    def __init__(self, index, previous_hash, timestamp, data, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.mine_block()

    def mine_block(self):
        prefix = "0" * self.difficulty
        while True:
            hash_candidate = hashlib.sha256(f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()
            if hash_candidate.startswith(prefix):
                return hash_candidate
            self.nonce += 1

class MiningBlockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = MiningBlock(0, "0", time.time(), "Genesis Block", self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, new_data):
        latest_block = self.chain[-1]
        new_block = MiningBlock(len(self.chain), latest_block.hash, time.time(), new_data, self.difficulty)
        self.chain.append(new_block)

# Example usage
mining_chain = MiningBlockchain(difficulty=4)
mining_chain.add_block("Mining Block 1 Data")
mining_chain.add_block("Mining Block 2 Data")

for block in mining_chain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Nonce: {block.nonce}")
