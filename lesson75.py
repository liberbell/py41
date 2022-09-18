from ssl import _Cipher
import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)
key = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

iv = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
print(key, iv)

cipher = AES.new(key, AES.MODE_CBC, iv)