import random
print('''OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
opcao = int(input('ESCOLHA UMA MÃO: '))
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
if opcao == 1:
    opcao = 'PEDRA'
    if computador == 'pedra':
        print(f"sua mão foi PEDRA e o computador escolheu {computador}")
        print('EMPATE!')
    elif computador == 'papel':
        print(f'sua mão foi PAPEL e o computador escolheu {computador}'.upper())
        print('Você perdeu!')
    elif computador == 'tesoura':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('Voce venceu!')
if opcao == 2:
    opcao = 'PAPEL'
    if computador == 'pedra':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('VOCÊ VENCEU !!!')
    elif computador == 'papel':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('EMPATE')
    elif computador == 'tesoura':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('Você perdeu!')
if opcao == 3:
    opcao = 'TESOURA'
    if computador == 'pedra':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('Você perdeu!')
    elif computador == 'papel':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('Você venceu!')
    elif computador == 'tesoura':
        print(f'sua mão foi {opcao} e o computador escolheu {computador}'.upper())
        print('EMPATE')
