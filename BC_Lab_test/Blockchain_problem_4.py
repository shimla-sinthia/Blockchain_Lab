#Task 4: Write a program in Python to implement a blockchain and print the values of all fields as described in etherscan.ioimport hashlib

import hashlib
import datetime

class Block:
    def __init__(self, block_number, transactions, previous_hash, gas_limit, gas_used, miner):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.miner = miner
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate SHA-256 hash of the block based on its attributes.
        """
        data_string = (
            str(self.block_number) +
            str(self.timestamp) +
            str(self.transactions) +
            str(self.previous_hash) +
            str(self.gas_limit) +
            str(self.gas_used) +
            str(self.miner)
        )
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a Genesis Block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (Genesis Block).
        """
        return Block(0, "Genesis Block", "0", 0, 0, "Genesis Miner")

    def add_block(self, new_block):
        """
        Add a new block to the blockchain.
        """
        new_block.previous_hash = self.chain[-1].hash  # Link to previous block
        new_block.hash = new_block.calculate_hash()  # Calculate the new block's hash
        self.chain.append(new_block)

    def print_block(self, block):
        """
        Print all details of a given block.
        """
        print(f"Block Number: {block.block_number}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Gas Limit: {block.gas_limit}")
        print(f"Gas Used: {block.gas_used}")
        print(f"Miner: {block.miner}")
        print(f"Hash: {block.hash}")
        print("-" * 50)

    def traverse_chain(self):
        """
        Print all blocks in the blockchain.
        """
        for block in self.chain:
            self.print_block(block)


# === Creating the Blockchain ===
my_blockchain = Blockchain()

# Adding new blocks with transactions, gas limits, and miner information
my_blockchain.add_block(Block(1, "Transaction 1", "", 1000000, 500000, "Miner 1"))
my_blockchain.add_block(Block(2, "Transaction 2", "", 2000000, 1500000, "Miner 2"))
my_blockchain.add_block(Block(3, "Transaction 3", "", 3000000, 2500000, "Miner 3"))

# Print all blocks
my_blockchain.traverse_chain()
