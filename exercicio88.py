from random import randint
jogos = []
soma = 0
quest = int(input('Quantos jogos você quer que eu sortei? '))
while True:
    if soma <= quest:
        dados = randint(1, 60)
        jogos.append(dados)
        soma += 1
    else:
        break
for i in range(1, quest + 1):
    print(f'Jogo {i}°: {jogos}')







