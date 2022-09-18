import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)
key = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

iv = "".join(
    random.choice(string.ascii_ßletters) for _ in range(AES.block_size)
)
print(key, iv)

plaintext = "fdseiourwaiogjhlkajfaslj"
cipher = AES.new(key, AES.MODE_CBC, iv)
padding_length = AES.block_size - len(plaintext) % AES.block_size

plaintext += chr(padding_length) * padding_length
chipher_text = cipher.encrypt(plaintext)
print(chipher_text)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher2.decrypt(chipher_text)