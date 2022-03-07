import hashlib
import time

start_time = time.time()
n = 1


def input1(x):
    data = "\x00" * int(x / 8)
    data = data.encode()
    return data


def collision(st, v, bit):
    while True:
        h2 = hashlib.sha256(bytes(v))
        st2 = h2.digest()
        # print(st2)
        if st[0:int(bit / 8)] == st2[0:int(bit / 8)]:
            print(bit, "- bit")
            print(v)
            print("hash1: ", st, "hash 2:", st2)
            break
        else:
            v = v + 1


m1 = input1(8)
collision(m1, n, 8)
end_time = time.time()
print("Time:", end_time - start_time)

