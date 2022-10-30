times = ('Corintians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os cinco primeiros são: {times[:5]}')
print('-=' * 30)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')


