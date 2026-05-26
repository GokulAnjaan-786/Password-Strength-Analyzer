import hashlib

def generate_hash(password):

    return hashlib.sha256(password.encode()).hexdigest()