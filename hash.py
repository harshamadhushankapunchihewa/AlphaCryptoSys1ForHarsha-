# Define the message X
X = "Exams are on red USB drive in JO 18.103. Password is CaKe314."


# Custom hash function
def custom_hash(message):
    # Convert message to bytes
    message_bytes = message.encode('utf-8')

    # Initialize a large prime number and an initial hash value
    prime = 31
    hash_value = 0

    # Iterate over each byte in the message
    for i, byte in enumerate(message_bytes):
        # XOR the byte with the current hash value and multiply by a prime
        hash_value ^= (byte * prime ** (i % 8))  # Simple transformation using primes and byte positions

        # Use a large prime modulo to limit the hash size
        hash_value %= 2 ** 64  # Keep the hash value within 64 bits

    # Convert the hash_value to a hexadecimal string and return
    return hex(hash_value)


# Generate the message digest (hash) using the custom function
message_digest = custom_hash(X)

# Print the message digest
print(f"Custom Hash for X: {message_digest}")

