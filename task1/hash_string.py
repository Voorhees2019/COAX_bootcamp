import hashlib


def hash_string(string: str) -> str:
    """Return hashed string using SHA256 algorithm."""
    return hashlib.sha256(string.encode()).hexdigest()


if __name__ == "__main__":
    s = "Python Bootcamp"
    print(hash_string(s))
