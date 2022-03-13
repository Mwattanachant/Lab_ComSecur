n = 0
generator = []


def is_generator(g, p):
    x = []
    check = False
    print("g:", g)
    for i in range(p - 1):
        x.append((g ** i) % p)
        print(g, "^", i, "=", x[i])
    for j in range(1, p - 1):
        if x[0] == x[j]:
            check = False
            break
        elif x[0] != x[j]:
            check = True
    return check


for k in range(1, 3):
    if is_generator(k, 127):
        n = n + 1
        generator.append(k)
print("Number of generators: ", n)
print("All generator:", generator)
