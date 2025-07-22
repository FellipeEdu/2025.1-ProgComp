import os, sys

strDirApp = os.path.dirname(__file__)

strNomeArq = f'{strDirApp}//cartola_fc_2024.json'

try:
    arqInput = open(strNomeArq, 'r',encoding='utf-8')
except FileNotFoundError:
    sys.exit('ERRO: Arquivo não existe.')
except Exception as erro:
    sys.exit(f'ERRO: {erro}.')
else:
    strDados = arqInput.read()
    # transformando em dicionario