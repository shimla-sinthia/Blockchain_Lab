from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError

# Generate two different key pairs
private_key1 = SigningKey.generate(curve=SECP256k1)
public_key1 = private_key1.verifying_key

private_key2 = SigningKey.generate(curve=SECP256k1)
# public_key2 = private_key2.verifying_key

message = b"Blockchain - Transaction"

signature = private_key1.sign(message)
signature = private_key2.sign(message)

# print("Signature:", signature.hex())
# Verify the signature with the correct public key
# is_valid = public_key1.verify(signature, message)

print("Message:", message.decode())
print("Signature:", signature.hex())
# print("Signature Verified:", is_valid)

try:
    is_valid = public_key1.verify(signature, message)
    print("Signature Verified :", is_valid)
except BadSignatureError:
    print("❌ Signature verification failed! Wrong public key used.")
