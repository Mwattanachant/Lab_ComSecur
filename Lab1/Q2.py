import string

c: string = input("Input e for encryption, d for decryption: ")
o: string = input("Input OTP: ")
p: string = input("Input plaintext:")
alp = string.ascii_lowercase
# print(alp)
if c == 'e':
    en = ""
    for k in range(len(o)):
        x = alp.find(p[k])
        ot = alp.find(o[k])
        n = (int(x) + int(ot)) % 26
        en = en + alp[n]
    print(en)
elif c == 'd':
    den = ""
    for k in range(len(o)):
        x = alp.find(p[k])
        ot = alp.find(o[k])
        n = (int(x) - int(ot)) % 26
        den = den + alp[n]
    print(den)


