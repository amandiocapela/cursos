from matplotlib import pyplot as plt
from faker import Faker
from random import randint
from time import sleep
from collections import Counter
from num2words import num2words
from wordcloud import WordCloud

# Criação de listas que serão usadas
leitura = []
nomes = []
pont = []
num = []

# Quantos nomes e números deverão ser criados aleatóriamente
n = int(input('Quantos nomes gostaria de gerar? '))
print('Gerando nomes e números aleatórios...')

# Gerar nomes e números aleatórios dentro de um arquivo txt
fake = Faker()
with open('dados.txt', 'w') as arquivo:
    for c in range(0, n):
        arquivo.write(f'{fake.name()},{str(randint(1, 10))},')

# Ler arquivo txt e lançar em uma lista para ser manipulado
with open('dados.txt', 'r') as arquivo:
    leitura = arquivo.read().split(',')
leitura.pop()  # Remover o último item da lista sendo um lixo gerado pela leitura

# Lançar nas listas separadas de nome e números (pontuações)
for c in range(0, (n*2), 2):
    nomes.append(leitura[c])
    pont.append(leitura[c + 1])

# Escrever o número por extenso e lançar em uma lista
for c in pont:
    num.append(num2words(c, lang='pt-br').title())

# Gerar uma string única para o wordcloud gerar a núvem
palavras = " ".join(p for p in num)
wordcloud = WordCloud(background_color="black").generate(palavras)

# Informar itens gerados
sleep(1)
print('Lista completa gerada:')
print(leitura)
sleep(0.5)
print('Nomes da lista gerada:')
print(nomes)
sleep(0.5)
print('Posição equivalente dos nomes gerados:')
print(pont)
sleep(0.5)
print('Número posição por extenso:')
print(num)

# Gerar gráficos
plt.subplot(2, 1, 1)
plt.hist(sorted(pont), label='Histograma das Pontuações')
plt.xlabel('Pontuações')
plt.ylabel('Probabilidade')
plt.grid(f'{Counter(pont)}')
plt.subplot(2, 1, 2)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
