import math
CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(CO, CA)

print(f'O cateto oposto digitado foi {CO}, o cateto adjacente digitado foi {CA} e a hipotenusa é {hi:.2f}')