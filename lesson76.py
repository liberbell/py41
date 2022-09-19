import hashlib
from hmac import digest

# print(hashlib.sha256(b"password").hexdigest())

user_name = "user1"
user_pass = "password"
db = {}

password = bytes(user_pass, "utf-8")
digest = hashlib.sha256(password).hexdigest()
db[user_name] = digest
print(db)