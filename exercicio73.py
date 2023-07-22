times = ('Botafogo','Palmeiras','Fluminense','Cruzeiro','Athletico','Atlético-MG',
        'Santos','Fortaleza','Flamengo','São Paulo','Grêmio','Internacional','Red Bull Bragantino',
         'Bahia','Goiás','Vasco','Corinthians','Cuiabá','Coritiba','América-MG')
print(f'Os cinco primeiros colocados são {times[:5]}')
print(f'Zona de rebaixmento {times[-4:]}')
print(f'Times em ordem alfabeica{sorted(times)}')
print(f"O time do Flamengo esta na {times.index('Flamengo')+1}ª colocação.")
