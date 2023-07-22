num = list()
impares = list()
pares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    escolha = str(input('Deseja continuas?[S/N] '))
    if escolha in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append((v))
print('-='* 30)
print(f'O total de valores da lista é {num}' )
print(f'Os valores pares são {pares}')
print(f'O valores impares são {impares}')


