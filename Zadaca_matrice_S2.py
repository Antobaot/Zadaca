import random
matrica = [[random.randint(1, 9) for _ in range(7)] for _ in range(7)]


for red in matrica:
    print(*red)



zbroj = sum(matrica[0]) + sum(matrica[6])  

for i in range(1, 6):  
    zbroj += matrica[i][0] + matrica[i][6]

print("Zbroj elemenata na rubovima matrice:", zbroj)
