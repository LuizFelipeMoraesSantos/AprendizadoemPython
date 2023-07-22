dados = [[], []]
for i in range(1, 8):
    numeros = int(input(f'Digite o {i}º número: '))
    if numeros % 2 == 0:
        dados[0].append(numeros)
    else:
        dados[1].append(numeros)
dados[0].sort()
dados[1].sort()
print(f'Todos os valores foram {dados[0]}')
print(f'Os valores pares foram {dados[1]}')
print(f'Os valores impar foram{dados}')

