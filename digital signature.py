import rsa

# Define the message X
X = "Exams are on red USB drive in JO 18.103. Password is CaKe314.".encode()

# Custom hash function (as defined earlier)
def custom_hash(message):
    message_bytes = message.encode('utf-8')
    prime = 31
    hash_value = 0

    for i, byte in enumerate(message_bytes):
        hash_value ^= (byte * prime ** (i % 8))
        hash_value %= 2 ** 64

    return hex(hash_value)

# Generate RSA public and private keys
(public_key, private_key) = rsa.newkeys(512)

# Create a digital signature using the private key with custom hash
message_hash = custom_hash(X)
signature = rsa.sign(message_hash.encode(), private_key, 'SHA-256')  # Use SHA-256 just for RSA signing

# Verify the signature using the public key
try:
    rsa.verify(message_hash.encode(), signature, public_key)
    print("The digital signature is valid.")
except rsa.VerificationError:
    print("The digital signature is not valid.")

# Print the digital signature
print(f"Digital Signature: {signature.hex()}")
