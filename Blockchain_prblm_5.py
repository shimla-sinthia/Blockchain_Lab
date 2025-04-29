# Task 5: Implementing a Blockchain and UTXO (Unspent Transaction Output)

import hashlib
import json
import time


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True)

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{[tx.to_json() for tx in self.transactions]}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = "0" * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.utxos = {}  # Unspent transaction outputs
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_transaction = Transaction("Genesis", "Network", 0)
        genesis_block = Block(0, "0", time.time(), [genesis_transaction])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        valid_transactions = []

        for tx in transactions:
            if self.is_valid_transaction(tx):
                valid_transactions.append(tx)
                self.update_utxos(tx)

        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), valid_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_valid_transaction(self, transaction):
        sender_balance = self.utxos.get(transaction.sender, 0)
        return sender_balance >= transaction.amount

    def update_utxos(self, transaction):
        # Deduct amount from sender
        if transaction.sender != "Genesis":
            self.utxos[transaction.sender] -= transaction.amount

        # Add amount to recipient
        if transaction.recipient not in self.utxos:
            self.utxos[transaction.recipient] = 0
        self.utxos[transaction.recipient] += transaction.amount

# Example usage
blockchain = Blockchain(difficulty=3)

# Adding transactions
transactions1 = [
    Transaction("Alice", "Bob", 50),
    Transaction("Bob", "Charlie", 30)
]
blockchain.utxos["Alice"] = 100  # Initialize Alice's balance
blockchain.add_block(transactions1)

transactions2 = [
    Transaction("Charlie", "Alice", 20),
    Transaction("Bob", "Alice", 10)
]
blockchain.add_block(transactions2)

# Display the blockchain
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print(f"Transactions: {[tx.to_dict() for tx in block.transactions]}")
    print("-" * 70)

# Display UTXOs
print("Unspent Transaction Outputs (UTXOs):")
for user, balance in blockchain.utxos.items():
    print(f"{user}: {balance}")
