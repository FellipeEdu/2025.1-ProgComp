import requests, sys

try:
    reqHTTP = requests.get('https://viacep.com.br/ws/13631-040/json')
except Exception as erro:
    print(f'ERRO: {erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('Erro na requisição.')
    
    dictCartola = reqHTTP.json()
    print(reqHTTP)
    print(dictCartola)