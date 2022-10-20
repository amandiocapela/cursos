n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua média foi {media:.1f} e você está reprovado.')
elif media >= 7.0:
    print(f'Sua média foi {media:.1f} e você está aprovado.')
else:
    print(f'Sua média foi {media:.1f} e você está de recuperação.')
    