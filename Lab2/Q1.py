from Crypto.Cipher import AES
import sys

key = "\x00" * 16
key = key.encode()
data = "\x00" * int(1.6 * 10 ** 8)
data = data.encode()

cipher = AES.new(key, AES.MODE_CBC, iv=key)
ciphertext = cipher.encrypt(data)

print(sys.getsizeof(ciphertext))
print(ciphertext[-16:].hex())
