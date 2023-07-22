from time import sleep
def maior(* num):
        print('\033[32mAnalisando os valores passados...')
        print('-=-' * 10)
        print('\033[mForam informados os valores', end='')
        maior = cont = 0
        for valor in num:
            if valor == maior:
                maior = valor
            if maior < valor:
                maior = valor
            cont += 1
            print(f' {valor}', end=" ")
            sleep(0.5)
        print(f'\nForam informados {cont} valores')
        print(f'O maior valor foi {maior}')
# Programa principal
maior(1, 5, 3, 7, 9, 0)

maior(4, 7, 8)
maior(2, 9)
maior()
