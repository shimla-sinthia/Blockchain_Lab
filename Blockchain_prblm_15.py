# Task 15: Proving Membership and Non-membership in a Merkle Tree

import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = [hashlib.sha256(tx.encode()).hexdigest() for tx in transactions]
        self.levels = self.build_merkle_levels(self.transactions)
        self.root = self.levels[-1][0] if self.levels else None

    def build_merkle_levels(self, transactions):
        levels = [transactions]
        while len(transactions) > 1:
            new_level = []
            for i in range(0, len(transactions), 2):
                left = transactions[i]
                right = transactions[i + 1] if i + 1 < len(transactions) else left
                combined = left + right
                new_level.append(hashlib.sha256(combined.encode()).hexdigest())
            levels.append(new_level)
            transactions = new_level
        return levels

    def get_proof(self, transaction):
        hashed_transaction = hashlib.sha256(transaction.encode()).hexdigest()
        if hashed_transaction not in self.levels[0]:
            raise ValueError("Transaction not in Merkle Tree")

        index = self.levels[0].index(hashed_transaction)
        proof = []

        for level in self.levels[:-1]:
            sibling_index = index ^ 1  # XOR to find sibling
            sibling = level[sibling_index] if sibling_index < len(level) else None
            proof.append((sibling, "left" if index % 2 else "right"))
            index //= 2

        return proof

    def verify_proof(self, transaction, proof, root):
        current_hash = hashlib.sha256(transaction.encode()).hexdigest()

        for sibling, direction in proof:
            if sibling:
                if direction == "left":
                    current_hash = hashlib.sha256((sibling + current_hash).encode()).hexdigest()
                else:
                    current_hash = hashlib.sha256((current_hash + sibling).encode()).hexdigest()

        return current_hash == root

# Example usage
transactions = ["tx1", "tx2", "tx3", "tx4"]
merkle_tree = MerkleTree(transactions)
print(f"Merkle Root: {merkle_tree.root}")

# Generating proof for a transaction
transaction_to_verify = "tx1"
proof = merkle_tree.get_proof(transaction_to_verify)
print(f"Proof for '{transaction_to_verify}': {proof}")

# Verifying the proof
is_valid = merkle_tree.verify_proof(transaction_to_verify, proof, merkle_tree.root)
print(f"Is the proof valid? {is_valid}")

# Verifying a non-membership proof
transaction_not_in_tree = "tx5"
try:
    proof = merkle_tree.get_proof(transaction_not_in_tree)
except ValueError as e:
    print(e)
