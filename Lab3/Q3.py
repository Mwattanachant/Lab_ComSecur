import hashlib
import hmac
# import binascii

# a = 6330613013 % 4
# print(a)

key = "4a6566654a6566654a6566654a6566654a6566654a6566654a6566654a656665"
key = bytearray.fromhex(key)


data = "7768617420646f2079612077616e7420666f72206e6f7468696e673f "
data = bytearray.fromhex(data)

hm = hmac.new(key,data,hashlib.sha256).hexdigest().lower()

print("PRF-HMAC-SHA-256 = " + hm)

# print("167f928588c5cc2eef8e3093caa0e87c9ff566a14794aa61648d81621a2a40c6")

