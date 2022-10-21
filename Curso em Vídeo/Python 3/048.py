n = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        cont += 1
        n += c
print(f'{cont} números são ímpares e a soma deles é {n}.')
