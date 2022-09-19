import string
import random
from tokenize import PlainToken

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)
key = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

iv = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# print(key, iv)

# plaintext = "fdseiourwaiogjhlkajfaslj"
with open("plaintext.txt", "r") as f, open("enc.dat", "wb")as e:
    plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size

    plaintext += chr(padding_length) * padding_length
    chipher_text = cipher.encrypt(plaintext)
    e.write(chipher_text)
# print(chipher_text)

with open("plaintext.txt", "rb") as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]])