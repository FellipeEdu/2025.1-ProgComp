import sys

try:
    numero = int(input('Digite um número inteiro positivo de até 4 dígitos: '))

    # verifica se o número tá no intervalo permitido (de 0 a 9999)
    if not (999 < numero <= 9999):
        sys.exit('ERRO: Digite um número positivo de até 4 algarismos!\n') 

    # soma dos dígitos
    soma = (numero % 10) + (numero // 10 % 10) + (numero // 100 % 10) + (numero // 1000 % 10)

except ValueError: # exceção se digitar um valor que nao é numero
    print('erro: digite um valor numérico.\n')
except Exception as e:  # exceção generica
    print(f'erro: {e}')
else:
    print(f'Soma dos algarismos é: {soma}')