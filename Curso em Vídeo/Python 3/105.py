def notas(*n, sit=False):
    """
    -> Função para analisar várias notas e trazer a situação.
    :param n: Uma ou mais notas
    :param sit: Opcional, indicando se deve trazer a situação ou não.
    :return: Dicionário com várias informações.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
#help(notas)
