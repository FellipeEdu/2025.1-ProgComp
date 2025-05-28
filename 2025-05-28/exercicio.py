'''
programa que solicite  numeros int aleatoriamente ate que se digite 0

quando for digitado 0, o programa deve informar

a) quantos numeros foram digitados
b) a soma dos inteiros positivos
c) media dos inteiros positivos

O valor 0 não deve ser considerado em nenhum dos itens acima
'''
'''import sys

try:
    contNumero = 0
    soma = 0
    numero = int(input('Digite um numero inteiro (Para sair do programa digite 0): '))
    while numero != 0:
        if numero > 0:
            soma += numero
            contNumero += 1
        numero = int(input('Digite outro numero inteiro (Para sair do programa digite 0): '))

except ValueError:
    sys.exit('ERRO: digite um valor numérico inteiro.')

except Exception as exc:
    sys.exit(f'ERRO: {exc}.')

else:
    media = soma / contNumero
    print(f'Soma: {soma}')
    print(f'Média da soma: {soma} / {contNumero} = {media:.0f}')''' 

# logica do prof 
import sys

contPositivos = 0
contNumeros = 0
soma = 0
numero = None

while numero != 0:
    try:
        numero = int(input('Digite um numero inteiro (Para sair do programa digite 0): '))

    except ValueError:
        sys.exit('ERRO: digite um valor numérico inteiro.')

    except Exception as exc:
        sys.exit(f'ERRO: {exc}.')

    else:
        if numero > 0:
            soma += numero
            contPositivos += 1

        if numero != 0:
            contNumeros += 1

print(f'Quantidade numeros inteiros: {contNumeros}')
print(f'Soma: {soma}')
print(f'Média da soma: {soma} / {contNumeros} = {soma/contNumeros}')