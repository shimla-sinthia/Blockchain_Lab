# Write a Program in Python to Verify Hash Properties


import hashlib

def calculate_hash(data):
    """
    Calculate the SHA-256 hash of the given data.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def verify_determinism(data):
    """
    Verify that the hash function produces the same hash for the same input.
    """
    hash1 = calculate_hash(data)
    hash2 = calculate_hash(data)
    if hash1 == hash2:
        print("Determinism Verified: The same input produces the same hash.")
    else:
        print("Determinism Failed: The same input produced different hashes.")

def verify_avalanche_effect(data1, data2):
    """
    Verify the avalanche effect: small changes in input produce vastly different hashes.
    """
    hash1 = calculate_hash(data1)
    hash2 = calculate_hash(data2)
    print(f"Hash of '{data1}': {hash1}")
    print(f"Hash of '{data2}': {hash2}")
    if hash1 != hash2:
        print("Avalanche Effect Verified: The hashes are significantly different.")
    else:
        print("Avalanche Effect Failed: The hashes are too similar.")

# Input from the user
input1 = input("Enter the first string: ")
input2 = input("Enter a slightly modified version of the first string: ")

# Verify hash properties
print("\n=== Verifying Determinism ===")
verify_determinism(input1)

print("\n=== Verifying Avalanche Effect ===")
verify_avalanche_effect(input1, input2)
