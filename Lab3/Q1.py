import hashlib
import time


start_time = time.time()
h1 = hashlib.sha256(b'abcdefghijklmnopqrstuvwxyz')
st1 = h1.hexdigest()
n = 1


def collision(st, v, bit):
    while True:
        h2 = hashlib.sha256(bytes(v))
        st2 = h2.hexdigest()
        if st[0:int(bit / 4)] == st2[0:int(bit / 4)]:
            print(bit,"- bit")
            print(v)
            print("hash1: ", st, "hash 2:", st2)
            break
        else:
            v = v + 1


collision(st1, n, 8)
end_time = time.time()
print("Time:", end_time - start_time)
collision(st1, n, 16)
end_time = time.time()
print("Time:", end_time - start_time)
collision(st1, n, 24)
end_time = time.time()
print("Time:", end_time - start_time)
collision(st1, n, 32)
end_time = time.time()
print("Time:", end_time - start_time)

