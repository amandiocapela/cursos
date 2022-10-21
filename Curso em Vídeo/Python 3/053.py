# Opção 1:
frase = input('Digite uma frase: ').strip().lower().replace(' ','')

fraseInv = frase[::-1]

if frase == fraseInv:
    print(f'A frase é um palíndromo!')
else:
    print(f'A frase não é um palíndromo!')

# Opção 2:
'''frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if frase == inverso:
    print(f'A frase é um palíndromo!')
else:
    print(f'A frase não é um palíndromo!')'''