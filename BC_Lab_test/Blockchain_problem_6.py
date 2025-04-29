# Task 6: Implementing Proof of Work (PoW) Algorithm

import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        """
        Initializes a new block.
        """
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Starts at 0 and increases during mining
        self.hash = self.generate_hash()

    def generate_hash(self):
        """
        Generates a SHA-256 hash of the block's contents.
        """
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
        return block_hash

    def mine_block(self, difficulty):
        """
        Implements Proof of Work (PoW): Finds a valid hash with required leading zeros.
        """
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.generate_hash()
        
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        """
        Initializes the blockchain with a Genesis Block.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Set PoW difficulty level

    def create_genesis_block(self):
        """
        Creates the first block (Genesis Block).
        """
        return Block("Genesis Block", "0")

    def get_latest_block(self):
        """
        Returns the most recently added block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Mines and adds a new block to the blockchain.
        """
        new_block.previous_hash = self.get_latest_block().hash  # Link new block to previous block
        new_block.mine_block(self.difficulty)  # Perform mining
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain by checking hashes and previous hash links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if hash is correct
            if current_block.hash != current_block.generate_hash():
                return False

            # Check if previous_hash matches actual previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# === Running the Blockchain with Proof-of-Work ===
if __name__ == "__main__":
    blockchain = Blockchain()

    print("\nMining block 1...")
    block1 = Block("Transaction 1", "")
    blockchain.add_block(block1)
    
    print("\nMining block 2...")
    block2 = Block("Transaction 2", "")
    blockchain.add_block(block2)

    print("\nMining block 3...")
    block3 = Block("Transaction 3", "")
    blockchain.add_block(block3)

    # Validate blockchain integrity
    print("\nIs blockchain valid? {}".format(blockchain.is_chain_valid()))

    # Tampering with blockchain data
    blockchain.chain[1].data = "Tampered transaction"

    # Revalidate blockchain after tampering
    print("\nIs blockchain valid after tampering? {}".format(blockchain.is_chain_valid()))
