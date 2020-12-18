import hashlib


def hash_password(password):
    return hashlib.sha3_256(password.encode()).hexdigest()
