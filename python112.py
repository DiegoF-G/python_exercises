import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except Exception as erro:
    print(f'{erro}O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(f'\nO respectivo HTML dele é:\n{site.read()}')
