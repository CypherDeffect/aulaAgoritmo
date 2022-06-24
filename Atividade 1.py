madmax = [[0, 0], [0, 0]]
rambo = [[0, 0], [0, 0]]
maior = -999999
for l in range(2):
    for c in range(2):
        madmax[l][c] = int(input(f"Informe o valor:"))
        if (m[l][c] > maior):
            maior = madmax[l][c]

for l in range(2):
    for c in range(2):
        rambo[l][c] = (madmax[l][c] * maior)
print(madmax)
print(rambo)
