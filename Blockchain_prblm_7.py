import hashlib
import random
import time

# Task 7: Implementing Proof of Stake (PoS) Consensus Algorithm
class Block:
    def __init__(self, index, previous_hash, timestamp, data, validator):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.validator}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class PoSBlockchain:
    def __init__(self):
        self.chain = []
        self.stakeholders = {}  # Address -> Stake
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), "Genesis Block", "System")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_stakeholder(self, address, stake):
        """Add a stakeholder with their stake amount."""
        if address in self.stakeholders:
            self.stakeholders[address] += stake
        else:
            self.stakeholders[address] = stake

    def select_validator(self):
        """Randomly select a validator based on their proportion of the total stake."""
        total_stake = sum(self.stakeholders.values())
        pick = random.uniform(0, total_stake)
        current = 0

        for address, stake in self.stakeholders.items():
            current += stake
            if current > pick:
                return address

    def add_block(self, data):
        """Adds a new block to the chain, validated by a chosen stakeholder."""
        validator = self.select_validator()
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, time.time(), data, validator)
        self.chain.append(new_block)
        print(f"Block added by validator: {validator}")

# Example usage
pos_chain = PoSBlockchain()

# Adding stakeholders
pos_chain.add_stakeholder("Alice", 50)
pos_chain.add_stakeholder("Bob", 30)
pos_chain.add_stakeholder("Charlie", 20)

# Adding blocks
pos_chain.add_block("Block 1 Data")
pos_chain.add_block("Block 2 Data")
pos_chain.add_block("Block 3 Data")

# Display the blockchain
for block in pos_chain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Validator: {block.validator}")
    print(f"Hash: {block.hash}")
    print("-" * 70)
