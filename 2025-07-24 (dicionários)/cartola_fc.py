import requests, sys

try:
    cep = input('digite um cep: ')
    reqHTTP = requests.get(f'https://viacep.com.br/ws/{cep}/json')
except Exception as erro:
    print(f'ERRO: {erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('Erro na requisição.')
    
    dictCartola = reqHTTP.json()
    #print(f'Status: {reqHTTP.status_code}')
    print(reqHTTP.json())
    #print(dictCartola)