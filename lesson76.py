import base64
from curses import has_il
from hmac import digest
import os
import hashlib

# print(hashlib.sha256(b"password").hexdigest())

user_name = "user1"
user_pass = "password"
db = {}

salt = base64.b64encode(os.urandom(32))
# print(salt)

# def get_digest(password):
#     password = bytes(password, "utf-8")
#     digest = hashlib.sha256(salt + password).hexdigest()
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, "utf-8")).hexdigest()
#         print(digest)
#     print(digest)
#     return digest

digest = hashlib.pbkdf2_hmac("sha256", bytes(user_pass, "utf-8"), salt, 10000)

db[user_name] = digest

# db[user_name] = get_digest(user_pass)

def is_login(user_name, password):
    digest = hashlib.pbkdf2_hmac("sha256", bytes(password, "utf-8"), salt, 10000)
    return digest == db[user_name]

print(is_login(user_name, user_pass))