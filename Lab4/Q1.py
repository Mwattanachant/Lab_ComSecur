
def is_generator(g, p):
    x = []
    for i in range(p):
        x.append((g ** i) % p)
    for j in range(1, p - 2):
        if j != 0:
            if x[0] == x[j]:
                return False
    return True


def defineGen(prime):
    n = 0
    generator = []
    for k in range(1, prime):
        if is_generator(k, prime):
            n = n + 1
            generator.append(k)
    print("Number of generators: ", n)
    print("All generator:", generator)


defineGen(23)
defineGen(127)
# defineGen(27)


