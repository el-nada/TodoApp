import hashlib
import os

def generate_salt():
    # Generate a random 16-byte salt
    return os.urandom(16).hex()

def hash_password(password, salt, iterations: int = 100000):
    # Combine password and salt
    salted_password = (password + salt).encode()
    
    # Apply key stretching using multiple iterations
    hashed = hashlib.pbkdf2_hmac(
        "sha256",  # Hash algorithm
        salted_password,  # Password + salt
        salt.encode(),  # Salt as bytes
        iterations  # Number of iterations
    )
    return hashed.hex()

def verify_password(stored_hash: str, input_password: str, salt: str) -> bool:
    # Hash the input password with the same salt
    input_hash = hash_password(input_password, salt)
    # Compare the hashes
    return input_hash == stored_hash