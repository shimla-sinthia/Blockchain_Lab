# Task 14: Write a program in Python to Create a Merkle Tree in Blockchain

import hashlib

def hash_node(data):
    """
    Returns the SHA-256 hash of the given data.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(leaves):
    """
    Builds a Merkle Tree from a list of leaves and returns the root.
    Also prints the tree level by level.
    """
    # Hash all leaves first
    tree = [[hash_node(leaf) for leaf in leaves]]

    # Build the tree level by level
    while len(tree[-1]) > 1:
        current_level = tree[-1]
        
        # Ensure even number of nodes by duplicating the last node if needed
        if len(current_level) % 2 == 1:
            current_level.append(current_level[-1])

        # Compute the next level by hashing pairs of nodes
        next_level = [hash_node(current_level[i] + current_level[i + 1]) for i in range(0, len(current_level), 2)]
        
        tree.append(next_level)

    return tree

def print_merkle_tree(tree):
    """
    Prints the Merkle Tree level by level.
    """
    print("\nMerkle Tree Structure (Level-wise):")
    for level in range(len(tree)):
        print(f"Level {level}: {tree[level]}")

# Example usage
leaves = ["apple", "banana", "cherry", "date"]

# Build the Merkle Tree
merkle_tree = build_merkle_tree(leaves)

# Print the tree level by level
print_merkle_tree(merkle_tree)

# Print the Merkle Root (Top Level)
print("\nMerkle Root:", merkle_tree[-1][0])
