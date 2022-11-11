from matplotlib import pyplot as plt
from faker import Faker
from random import randint
from time import sleep
from collections import Counter
from num2words import num2words
from wordcloud import WordCloud


nomes = []
pont = []
num = []

fake = Faker()
n = int(input('Quantos nomes gostaria de gerar? '))
print('Gerando nomes e números aleatórios...')
sleep(2)

with open('dados.txt', 'w') as arquivo:
    for c in range(0, n):
        arquivo.write(f'{fake.name()},{str(randint(1, 10))},')


with open('dados.txt', 'r') as arquivo:
    a = arquivo.read().split(',')
a.pop()

for c in range(0, (n*2), 2):
    nomes.append(a[c])
    pont.append(a[c+1])

for c in pont:
    num.append(num2words(c, lang='pt-br').title())

palavras = " ".join(p for p in num)
wordcloud = WordCloud(background_color="black").generate(palavras)

print('Lista completa gerada:')
print(a)
sleep(1)
print('Nomes da lista gerada:')
print(nomes)
sleep(1)
print('Posição equivalente dos nomes gerados:')
print(pont)
print('Número posição por extenso:')
print(num)

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
