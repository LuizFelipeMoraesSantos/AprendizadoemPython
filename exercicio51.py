primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(c, end='-> ')
print('Acabou')
