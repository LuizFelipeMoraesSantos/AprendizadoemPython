print('CONTROLE DE TERRENOS')
print('--------------------')
def area(l,c):
    terreno = l*c
    return terreno


l = float(input('Largura do terreno: '))
c = float(input('Comprimento do terreno: '))
print(f'A area de um terreno de {l} m x {c} m é de { area(l , c)} m²')