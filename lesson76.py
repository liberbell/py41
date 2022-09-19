import base64
import os
import hashlib

# print(hashlib.sha256(b"password").hexdigest())

user_name = "user1"
user_pass = "password"
db = {}

salt = base64.b64encode(os.urandom(32))
# print(salt)

def get_digest(password):
    password = bytes(password, "utf-8")
    digest = hashlib.sha256(salt + password).hexdigest()
    print(digest)
    return digest

db[user_name] = get_digest(user_pass)

def is_login(user_name, password):
    return get_digest(password) == db[user_name]

print(is_login(user_name, "passwords"))