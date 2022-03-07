# c1 xor c2 xor p1
def strings_xor(C1,C2,P1):
    a_list = []
    for i in range(len(C1)):
        a_list += chr(ord(C1[i]) ^ ord(C2[i]) ^ ord(P1[i]))
    return a_list

# c
c1 = "8f298d0642d1460605058cfbfcce4868"

# c'
c2 = "9439910f5fb91302081eacbef6cf0d71"

p1 = "48656c6c6f2c2074686973206973206d"


p = strings_xor(c1,c2,p1)
p2 = "".join(p)
print(p2)