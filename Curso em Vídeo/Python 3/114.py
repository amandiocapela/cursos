import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
