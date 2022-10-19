from math import radians, sin, cos, tan

n = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))

print(f'O ângulo de {n} tem o SENO de {sen:.2f}')
print(f'O ângulo de {n} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {n} tem a TANGENTE de {tan:.2f}')
