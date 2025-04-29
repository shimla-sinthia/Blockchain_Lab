# Task 8: Write a program in Python to Fetch the Latest Block Information from Ethereum Blockchain Using Etherscan API


import requests

def get_latest_block(api_key):
    """
    Fetch the latest block information from Ethereum blockchain using Etherscan API.
    """
    url = "https://api.etherscan.io/api"

    # Define API request parameters
    params = {
        "module": "proxy",  # Access the Ethereum JSON-RPC API via Etherscan
        "action": "eth_getBlockByNumber",  # Fetch block details by number
        "tag": "latest",  # Get the latest block
        "boolean": "true",  # Return full transaction details
        "apikey": api_key,  # Your Etherscan API key
    }

    try:
        # Send GET request to Etherscan API
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Convert response to JSON format
            return data["result"]  # Extract block information
        else:
            print("Request failed with status code:", response.status_code)

    except requests.RequestException as e:
        print("Request failed:", str(e))

    return None  # Return None if the request fails

# Replace "YOUR_API_KEY" with your actual Etherscan API key
api_key = "E34342B4IR3B8RI3K61XG4YKEUT7SR54MM"

# Fetch the latest block details
latest_block = get_latest_block(api_key)

# Print block details if successfully fetched
if latest_block is not None:
    print("\n=== Latest Block Information ===")
    print("Block Number:", int(latest_block["number"], 16))  # Convert hex to decimal
    print("Timestamp:", int(latest_block["timestamp"], 16))
    print("Miner Address:", latest_block["miner"])
    print("Difficulty:", int(latest_block["difficulty"], 16))
    print("Total Difficulty:", int(latest_block["totalDifficulty"], 16))
    print("Gas Limit:", int(latest_block["gasLimit"], 16))
    print("Gas Used:", int(latest_block["gasUsed"], 16))
    print("Transaction Count:", len(latest_block["transactions"]))
    
    print("\n=== Transactions in Latest Block ===")
    for tx in latest_block["transactions"][:5]:  # Display only first 5 transactions
        print(f"Transaction Hash: {tx['hash']}")
        print(f"From: {tx['from']}")
        print(f"To: {tx['to']}")
        print(f"Value (in Wei): {tx['value']}")
        print("-" * 50)
else:
    print("Failed to fetch the latest block information.")
