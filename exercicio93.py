dados = {}
part = 0
soma = []
dados["nome"] = input('Nome do jogador: ')
part = int(input('Quantas partidas jogadas: '))
for v in range(1, part + 1):
    soma.append(int(input(f"Quantos gols na partida {v}º: ")))
    dados.copy(soma["gols"])
print("-=-"*15)
print(dados)