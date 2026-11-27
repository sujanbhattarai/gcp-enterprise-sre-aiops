import hashlib

def security_test():
    return hashlib.md5(b"demo-security-test").hexdigest()
