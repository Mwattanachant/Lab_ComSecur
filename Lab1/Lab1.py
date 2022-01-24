import string

c: string = input("Input e for encryption, d for decryption: ")
m = input("Input message: ")
k = int(input("Input Key: "))
alp = string.ascii_lowercase

if c == 'e':
    encry = ""
    for i in m:
        x = alp.find(i)
        n: int = (int(x) + int(k)) % 26
        encry = encry + alp[n]
    #     new = x + k
    #     encry += alp[new]
    print(encry)
elif c == 'd':
    dencry = ""
    for i in m:
        x = alp.find(i)
        n: int = (int(x) - int(k)) % 26
        dencry = dencry + alp[n]
    #     new = x + k
    #     encry += alp[new]
    print(dencry)
