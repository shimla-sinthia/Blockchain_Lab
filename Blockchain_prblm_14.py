# Write a program in Python to Create a Merkle Tree in Blockchain

import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_merkle_tree(transactions)

    def build_merkle_tree(self, transactions):
        if len(transactions) == 1:
            return hashlib.sha256(transactions[0].encode()).hexdigest()

        new_level = []
        for i in range(0, len(transactions), 2):
            left = transactions[i]
            right = transactions[i + 1] if i + 1 < len(transactions) else left
            new_level.append(hashlib.sha256((left + right).encode()).hexdigest())

        return self.build_merkle_tree(new_level)

# Example usage
transactions = ["tx1", "tx2", "tx3", "tx4"]
merkle_tree = MerkleTree(transactions)
print(f"Merkle Root: {merkle_tree.root}")
