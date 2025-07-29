from logging import exception
import funcoes

try:
    intE1 = int(input('Informe E1: '))
    intE2 = int(input('Informe E2: '))
except ValueError:
    print('ERRO: Informe inteiro válido')
except Exception as erro:
    print(f'ERRO: {erro}')
else:
    try:
        mediaFinal = funcoes.mediaIFRN(intE1, intE2)
    except Exception as erro:
        print(erro)
    else:
        print(f'MÉDIA = {mediaFinal}')