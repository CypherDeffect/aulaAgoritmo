import numpy as np
import random

notas = np.zeros(shape=(10, 3))
menores_notas_prova = [0, 0, 0]

for numero_aluno in range(10):
    for nota_aluno in range(3):
        print("Digite a nota ", nota_aluno, "para o aluno ", numero_aluno, ": ")
        notas[numero_aluno][nota_aluno] = float(input())

print(notas)

for numero_aluno in range(10):
    prova = 0
    menor = 11
    for nota_aluno in range(3):
        if (notas[numero_aluno][nota_aluno] < menor):
            menor = notas[numero_aluno][nota_aluno]
            prova = nota_aluno
    print("ALUNO ", numero_aluno)
    print("MENOR NOTA NA PROVA ", prova, "COM NOTA ", menor)
    menores_notas_prova[prova] += 1

for i in range(3):
    print("Alunos que tiveram menor nota na prova ", i, ": ", menores_notas_prova[i])


