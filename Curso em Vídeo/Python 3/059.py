n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

escolha = 0

while escolha != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Qual é a sua opção? '))

    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}!')
        print('=-=' * 10)
    if escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}!')
        print('=-==-==-==-==-==-==-==-==-==-=')
    if escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}!')
            print('=-=' * 10)
        else:
            print(f'{n2} é maior que {n1}!')
            print('=-=' * 10)
    if escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if escolha == 5:
        print('Encerrando o programa...')
        print('=-=' * 10)
    else:
        print('Opção invalida. Tente novamente.')
print('Fim do programa!')

