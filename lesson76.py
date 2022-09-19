import hashlib
from hmac import digest

# print(hashlib.sha256(b"password").hexdigest())

user_name = "user1"
user_pass = "password"
db = {}

def get_digest(password):
    password = bytes(user_pass, "utf-8")
    digest = hashlib.sha256(password).hexdigest()
    return digest

db[user_name] = get_digest(user_pass)

def is_login(user_name, password):
    return get_digest(password)
    
print(db)