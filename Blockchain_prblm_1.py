#Write a program in Python to implement blockchain.

import hashlib
import json
import time
from typing import List

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash}, prev_hash={self.previous_hash})"


def calculate_hash(index, previous_hash, timestamp, data):
    return hashlib.sha256(f"{index}{previous_hash}{timestamp}{data}".encode()).hexdigest()


def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))


def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash_value = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash_value)


# Task 1: Implement a Blockchain
class Blockchain:
    def __init__(self):
        self.chain: List[Block] = [create_genesis_block()]

    def add_block(self, data):
        new_block = create_new_block(self.chain[-1], data)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)


# Creating blockchain and adding blocks
blockchain = Blockchain()
blockchain.add_block("First Block")
blockchain.add_block("Second Block")
blockchain.print_chain()