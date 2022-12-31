from time import sleep

def maior(* valores):
    qtd = len(valores)
    print('~' * 50)
    for c in range(0, qtd):
        print(f'{valores[c]}', end=' ')
        sleep(0.25)
    print(f'Foram informados {qtd} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}.')
    print('~' * 50)


#Programa Principal
maior(1, 2, 3, 5)
maior(1, 5, 4, 10, 28, 100, 1000, 2)
