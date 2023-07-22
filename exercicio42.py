lado1 = int(input('Digite lado A: '))
lado2 = int(input('Digite lado B: '))
lado3 = int(input('Digite o lado C: '))

if lado1 == lado2 == lado3:
    print('Esse triângulo é EQUILÁTERO')
if lado1 != lado2 != lado3:
    print('Esse triângulo é ESCALENO')
if lado1 == lado2 != lado3 or lado2 == lado3 != lado1:
    print('Esse triângulo é ISÓSCELES')
else:
    print('Não form nem um tipo de triângulo')
