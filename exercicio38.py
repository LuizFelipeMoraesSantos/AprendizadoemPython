num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print(f'O número {num1} é maior.')
elif num2 > num1:
    print(f'O número {num2} é maior.')
else:
    print(f'O número {num1} e {num2} são iguais.')