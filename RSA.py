import rsa

try:
    # Generate RSA key pair (2048-bit)
    private_key, public_key = rsa.newkeys(2048)

    # Debugging: Print key types
    print(f"Private Key Type: {type(private_key)}")
    print(f"Public Key Type: {type(public_key)}")

    # Ensure keys are of the correct type
    if not isinstance(private_key, rsa.PrivateKey) or not isinstance(public_key, rsa.PublicKey):
        raise ValueError("Invalid key types. Ensure private_key and public_key are correctly assigned.")

except Exception as e:
    print(f"Error generating keys: {e}")
    exit(1)

# Function to create a digital signature
def create_signature(message, private_key):
    try:
        signature = rsa.sign(message.encode(), private_key, 'SHA-256')
        return signature
    except Exception as e:
        print(f"Error signing message: {e}")
        return None

# Function to verify the digital signature
def verify_signature(message, signature, public_key):
    try:
        rsa.verify(message.encode(), signature, public_key)
        print("Signature is valid.")
    except rsa.VerificationError:
        print("Signature is invalid.")
    except Exception as e:
        print(f"Error verifying signature: {e}")

# Message to be signed
message = "Hello, World!"

# Create digital signature
signature = create_signature(message, private_key)

if signature:
    print("Digital Signature:", signature.hex())  # Print in hex format for readability
    # Verify the digital signature
    verify_signature(message, signature, public_key)
