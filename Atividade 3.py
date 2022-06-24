import random

mat = [ [0]*20 ] * 10
soma = [0]*10

for i in range(0,10):
  for j in range(0,20):
    mat[i][j] = random.randint(1,10) #preenchi com valores aleatórios para não ter que digitar todos
    soma[i] = soma[i] + mat[i][j]


for i in range(0,10):
  for j in range(0,20):
    mat[i][j] = mat[i][j] * soma[i]

for i in range(0,10):
  for j in range(0,20):
    print(f"{i} - {j}:", mat[i][j])