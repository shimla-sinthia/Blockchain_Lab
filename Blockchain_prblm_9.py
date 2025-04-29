# Write a Python Program that Takes a String and the Desired Number of Leading Zeros from the User and Outputs the Input String, the Nonce Value for Which the Leading Zeros Puzzle Is Solved, and the Corresponding Hash Generated



import hashlib

def find_nonce(input_string, difficulty):
    nonce = 0
    prefix = "0" * difficulty  # Required leading zeros

    while True:
        # Combine input string with nonce and hash it
        data = input_string + str(nonce)
        hash_result = hashlib.sha256(data.encode()).hexdigest()

        # Check if hash meets the difficulty requirement
        if hash_result.startswith(prefix):
            return nonce, hash_result
        
        nonce += 1  # Increment nonce and try again

# Get user input
input_string = input("Enter a string: ")
difficulty = int(input("Enter the number of leading zeros required: "))

# Find the valid nonce and hash
nonce, final_hash = find_nonce(input_string, difficulty)

# Output results
print("\n=== Proof-of-Work Solved ===")
print(f"Input String: {input_string}")
print(f"Nonce: {nonce}")
print(f"Generated Hash: {final_hash}")
