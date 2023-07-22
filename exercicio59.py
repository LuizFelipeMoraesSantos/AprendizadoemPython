from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = maior = 0

while escolha != 5:
    print('''[1] soma
[2] multiplicação
[3] maior
[4] novos números
[5] sair do programa''')
    escolha = int(input('>>>>> Escolha uma opção: '))
    if escolha == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, n1 + n2))
        print(30 * '=')
    elif escolha == 2:
        print('A multiplicação de {} x {} = {} '.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O valor maior entre {} e {} é {}'.format(n1, n2 , maior))

    elif escolha == 4:
        print('Digite Novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif escolha == 5:
        print('Finalização do programa!!')
    else:
        print('Opção invalida!')
    sleep(2)
print('Muito Obrigado! Volte sempre. ')
