from Crypto.Cipher import AES
import imageio

Key = "\x00" * 16
Key = Key.encode()


def myEnc(key, msg):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)


def myEnc2(key, msg):
    cipher = AES.new(key, AES.MODE_CBC, iv=key)
    return cipher.encrypt(msg)


def myEnc3(key, msg):
    cipher = AES.new(key, AES.MODE_CFB, iv=key)
    return cipher.encrypt(msg)


img = imageio.imread('Blk.BMP')
dataVector = img.flatten()
dataBytes = bytes(dataVector)
print(len(dataBytes) % 16)

m = myEnc(Key, dataBytes)
m2 = myEnc2(Key, dataBytes)
m3 = myEnc3(Key, dataBytes)
print(m)
print(m2)
print(m3)
# with open('k.BMP','wb') as f:
#     f.write(dataBytes[0:120] + m + dataBytes[-154:])
