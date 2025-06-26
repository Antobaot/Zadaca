def generator_parnih(broj):
    for i in range(broj):
        if i % 2 == 0:
            yield i

def generator_neparnih(broj):
    for i in range(broj):
        if i % 2 != 0:
            yield i

n = int(input("Unesi gornju granicu: "))

print("Parni brojevi:")
g_parni = generator_parnih(n)
while 1:
    try:
        x = next(g_parni)
        print(x)
    except StopIteration:
        break

print("Neparni brojevi:")
g_neparni = generator_neparnih(n)
while 1:
    try:
        x = next(g_neparni)
        print(x)
    except StopIteration:
        break
