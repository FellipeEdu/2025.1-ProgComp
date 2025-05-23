'''try:
    intNum = int(input('Digite algo:'))
except:
    print('valor invalido')
else:
    print(intNum)
'''
import sys

try:
    intDividendo = int(input('Digite o dividendo:'))
    intDivisor = int(input('Digite o dividendo:'))
    
    floatResultado = intDividendo / intDivisor

except ValueError:  # exceção expecifica, nesse caso, de tipo de valor
    print('ERRO: informe um valor que possa ser convertido em inteiro')

except ZeroDivisionError: # exceção pra divisao por zero
    print('ERRO: não existe divisão por zero')

except '''Exception as tipoExcecao''' :        # passando a informação da exceção pra uma variavel
    print(f'ERRO: {sys.exc_info()}')    # exibe uma informação mais detalhada do erro -> "<class 'ValueError'>, ValueError("erro"), <traceback>"
#    print(f'ERRO: {tipoExcecao}')      # exibe apenas a informação do que foi o erro -> "erro"

else:
    print(floatResultado)