contagem =('zero', 'um', 'dois', 'tres', 'Quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dizesseis', 'dizessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        print(f'O número que você digitou foi {contagem[num]}')
    escolha = str(input('Quer tentar novamente [S/N]: ')).upper()[0]
    if escolha == 'S':
        num = int(input('Digite um número: '))
    if escolha == 'N':
        break
print('\033[35mPrograma encerrado.')



