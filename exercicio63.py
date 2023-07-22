'''print('Contador de números')
print('~'*20)
contador = 0
numero = int(input('Digite um número[ 999 para PARAR]: '))
soma = numero
while numero < 999:
    numero = int(input('Digite um número[ 999 para PARAR ]:  '))
    contador += 1
    soma = soma + numero
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, soma - 999))'''
num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número: '))
print('Você digitou {} e a soma entre eles foi {}'.format(cont, soma))