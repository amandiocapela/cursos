from matplotlib import pyplot as plt
from faker import Faker
from random import randint

fake = Faker()
n = int(input('Quantos nomes gostaria de gerar? '))

with open('dados.txt', 'w') as arquivo:
    for c in range(0, n):
        arquivo.write(fake.name() + ', ' + str(randint(1, n+1)) + '; ')

nomes = []
pont = []

with open('dados.txt', 'r') as arquivo:
    a = arquivo.read().split(';')

print(a)
