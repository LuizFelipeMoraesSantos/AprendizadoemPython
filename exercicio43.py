peso = float(input("PESO EM (KG): "))
altura = float(input("ALTURA EM (M): "))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'Seu Imc é {imc:.2f}, você esta ABAIXO DO PESO.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC é {imc:.2f}, você está no PESO IDEAL.')
if imc >= 25 and imc <= 29.9:
    print(f'Seu IMC é {imc:.2f}, você está com SOBREPESO. ')
elif imc >= 30 and imc <= 39.9:
    print(f'Seu IMC é {imc:.2f}, você está com OBESIDADE. ')
if imc >= 40:
    print(f'Seu IMC é {imc:.2f}, você está com OBESIDADE MORBIDA. ')