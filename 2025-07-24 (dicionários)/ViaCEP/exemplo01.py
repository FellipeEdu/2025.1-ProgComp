import requests, sys

cep = input('digite um cep: ')

try:
    reqHTTP = requests.get(f'https://viacep.com.br/ws/{cep}/json')
except Exception as erro:
    print(f'ERRO: {erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('Erro na requisição.')
    
    print(f'\n{reqHTTP}\n')
    #print(f'Status: {reqHTTP.status_code}')
    print(f'{reqHTTP.json()}')