#Task 2: Write a program in Python for mining a new block in a blockchain, and print the values of the new block.

import hashlib
import json
import time
from typing import List

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash}, prev_hash={self.previous_hash}, nonce={self.nonce})"


def calculate_hash(index, previous_hash, timestamp, data, nonce):
    return hashlib.sha256(f"{index}{previous_hash}{timestamp}{data}{nonce}".encode()).hexdigest()


def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block", 0))


def mine_block(previous_block, data, difficulty=4):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0
    hash_value = calculate_hash(index, previous_block.hash, timestamp, data, nonce)
    while not hash_value.startswith("0" * difficulty):
        nonce += 1
        hash_value = calculate_hash(index, previous_block.hash, timestamp, data, nonce)
    return Block(index, previous_block.hash, timestamp, data, hash_value, nonce)


# Task 1: Implement a Blockchain
class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [create_genesis_block()]

    def add_block(self, data):
        new_block = mine_block(self.chain[-1], data)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)
            print("-" * 50)


# Creating blockchain and mining blocks
blockchain = Blockchain()
print()
blockchain.add_block("First Block")
blockchain.add_block("Second Block")
blockchain.print_chain()