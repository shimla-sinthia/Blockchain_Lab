from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError
import random
# Generate two different key pairs
# private_key1 = SigningKey.generate(curve=SECP256k1)
private_keys = []
for i in range(5):
    private_keys.append(SigningKey.generate(curve=SECP256k1))
    
public_keys = []
for private_key in private_keys:
    public_keys.append(private_key.verifying_key)


messages = []
for i in range(5):
    messages.append(b"Blockchain" + str(i).encode())
    # print("Messages:", messages[i])
signatures = []
for i in range(5):
    signatures.append(private_keys[i].sign(messages[i]))
    print(signatures[i].hex())

for i in range(5):
  id = random.randint(0, i)
  try:
      is_valid = public_keys[i].verify(signatures[id], messages[i])
      print("Signature Verified :", is_valid)
  except BadSignatureError:
      print("❌ Signature verification failed! Wrong public key used.")
