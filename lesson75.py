import string
import random

from Crypto.Cipher import AES

key = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)