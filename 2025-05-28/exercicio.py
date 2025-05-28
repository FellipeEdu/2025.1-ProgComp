'''
programa que solicite  numeros int aleatoriamente ate que se digite 0

quando for digitado 0, o programa deve informar

a) quantos numeros foram digitados
b) a soma dos inteiros positivos
c) media dos inteiros positivos

O valor 0 não deve ser considerado em nenhum dos itens acima
'''
import sys

try:
    # contInt = 0
    contNumero = 0
    soma = 0
    numero = int(input('Digite um numero inteiro: \nPara sair do programa digite 0.'))
    while numero != 0:
        if numero > 0:
            contNumero += 1
            soma += numero

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    media = soma / contNumero 