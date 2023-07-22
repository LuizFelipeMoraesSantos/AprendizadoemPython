matriz = [[0,0,0], [0,0,0], [0,0,0]]
parS = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número[{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
        if matriz[l][c] % 2 == 0:
            parS += matriz[l][c]
    print()
print(f'A soma dos valores pares são {parS}')
coluna_3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma da terceira coluna é {coluna_3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')



