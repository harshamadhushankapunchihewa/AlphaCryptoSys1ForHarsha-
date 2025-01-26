import random
from math import gcd

# Function to calculate the modular inverse of e mod φ(n)
def mod_inverse(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None

# Function to generate a random prime number greater than 20
def generate_prime():
    while True:
        num = random.randint(21, 100)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            return num

# Function to perform RSA encryption
def encrypt_rsa(plain_text, e, n):
    encrypted_text = [pow(ord(char), e, n) for char in plain_text]
    return encrypted_text

# Function to perform RSA decryption
def decrypt_rsa(cipher_text, d, n):
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_text

# Generate prime numbers p and q
p = generate_prime()
q = generate_prime()

# RSA modulus
n = p * q

# Euler's totient function
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 65537  # This is a commonly used value for e
if gcd(e, phi) != 1:
    raise ValueError("e and phi(n) are not coprime!")

# Compute the private key d (modular inverse of e)
d = mod_inverse(e, phi)

# Define the symmetric cipher key K (for example, "cake")
K = "cake"

# Encrypt the key K using RSA
encrypted_key = encrypt_rsa(K, e, n)
print(f"Encrypted key (cipher text): {encrypted_key}")

# Decrypt the encrypted key to recover K
decrypted_key = decrypt_rsa(encrypted_key, d, n)
print(f"Decrypted key (plain text): {decrypted_key}")

# Display RSA parameters
print(f"p = {p}, q = {q}")
print(f"n = {n}")
print(f"e = {e}")
print(f"d = {d}")
