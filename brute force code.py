import random
import math
import time

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def brute_force_mod_inverse(e, phi):
    # Try all possible values for d from 3 to phi - 1
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

# Start measuring time
start_time = time.time()

# Generate primes p and q
p = generate_prime(1000, 5000)
q = generate_prime(1000, 5000)

# Ensure p and q are different
while p == q:
    q = generate_prime(1000, 5000)

n = p * q
phi_n = (p - 1) * (q - 1)

# Generate e
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

# Calculate d using brute force
d = brute_force_mod_inverse(e, phi_n)

end_time = time.time()
total_time = end_time - start_time

# Print keys and other values
print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p:", p)
print("q:", q)
print("Time taken: {:.4f} seconds".format(total_time))

# Optional: Encrypt and decrypt a message (if desired)
message = "Hello World"
def encrypt(message, e, n):
    message_bytes = message.encode('utf-8')
    encrypted = [pow(byte, e, n) for byte in message_bytes]
    return encrypted

def decrypt(encrypted, d, n):
    decrypted_bytes = [pow(byte, d, n) for byte in encrypted]
    decrypted_message = bytes(decrypted_bytes).decode('utf-8')
    return decrypted_message

# Encrypt and decrypt the message
encrypted_message = encrypt(message, e, n)
decrypted_message = decrypt(encrypted_message, d, n)

print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
