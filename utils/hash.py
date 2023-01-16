import hashlib

def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()[:20]