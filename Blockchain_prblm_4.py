#Write a program in Python to implement a blockchain and print the values of all fields as described in etherscan.ioimport hashlib

import json
import hashlib
import time
from typing import List

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash
        self.nonce = nonce

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash}, prev_hash={self.previous_hash}, nonce={self.nonce})"
    
    def print_block(self):
        print(json.dumps({
            "Block Number": self.index,
            "Previous Block Hash": self.previous_hash,
            "Timestamp": self.timestamp,
            "Nonce": self.nonce,
            "Block Hash": self.hash,
            "Transactions": self.transactions
        }, indent=4))


def calculate_hash(index, previous_hash, timestamp, transactions, nonce):
    return hashlib.sha256(f"{index}{previous_hash}{timestamp}{transactions}{nonce}".encode()).hexdigest()


def create_genesis_block():
    return Block(0, "0", int(time.time()), [{"from": "network", "to": "genesis", "amount": 0}], calculate_hash(0, "0", int(time.time()), [], 0))


def mine_block(previous_block, transactions, difficulty=4):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0
    hash_value = calculate_hash(index, previous_block.hash, timestamp, transactions, nonce)
    while not hash_value.startswith("0" * difficulty):
        nonce += 1
        hash_value = calculate_hash(index, previous_block.hash, timestamp, transactions, nonce)
    return Block(index, previous_block.hash, timestamp, transactions, hash_value, nonce)


# Task 1: Implement a Blockchain
class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [create_genesis_block()]

    def add_block(self, transactions):
        new_block = mine_block(self.chain[-1], transactions)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            block.print_block()


# Task 4: Print Blockchain Details Similar to Etherscan
blockchain = Blockchain()
blockchain.add_block([{"from": "Alice", "to": "Bob", "amount": 10}])
blockchain.add_block([{"from": "Bob", "to": "Charlie", "amount": 5}])
blockchain.add_block([{"from": "Charlie", "to": "David", "amount": 2}])
blockchain.add_block([{"from": "David", "to": "Eve", "amount": 8}])

# Print all blocks with full details
blockchain.print_chain()