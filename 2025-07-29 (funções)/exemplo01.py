from logging import exception
import sys, funcoes

try:
    intE1 = int(input('Informe E1: '))
    intE2 = int(input('Informe E2: '))
except ValueError:
    sys.exit('ERRO: Informe inteiro válido')
except Exception as erro:
    sys.exit(f'ERRO: {erro}')
else:
    try:
        mediaFinal = funcoes.mediaIFRN(intE1, intE2)
    except Exception as erro:
        print(erro)
    else:
        print(f'MÉDIA = {mediaFinal}')
        print(f'SITUAÇÃO: {funcoes.situacaoFinal(mediaFinal)}')