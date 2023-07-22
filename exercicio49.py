from time import sleep
num = int(input('Escolha um número: '))
for c in range(1, 11):
    mult = c * num
    print(c,' x ', num, '= ',mult)
    sleep(0.5)
