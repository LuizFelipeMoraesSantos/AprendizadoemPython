from random import randint
computador = randint(0, 10)
print('O computador vai sortear um número de 0 até 10')
print('Séra que voce consegue acertar o número sorteado?')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpites += 1
    if computador == acertou:
        acertou = True
print('Você acertou com {} tentatias! Parabéns.'.format(palpites))





# Como eu fiz.
'''import random
from random import randint
jog = 0
comp = 0
tentativas = 0
campeao = 0
while jog == campeao:
    jog = int(input('Digite um número de 1 até 10: '))
    comp = random.randint(1, 10)
    campeao = 
    if jog == comp:
        tentativas += 1
        print('PAREBÉNS VOCÊ É O VENCEDOR !!!')
        print(' Você tentou {} vezes.'.format(tentativas))
    if jog != comp:
            print('tente mais uma vez')
    print('Você digitou {}  e o número sorteado foi {}.'.format(jog, comp))'''



