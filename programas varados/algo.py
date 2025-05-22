# vou fazer alguma coisa aq

# print('testando o commit\n')

'''
numero = int(input('Digite seu numero:'))
nome = (input('digite seu nome:'))

print('seu nome e numero é: ', nome, '-', numero)
'''
# print(chr(10084)) # emoji de coração (caractere unicode)
import sys

ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ladoC = float(input('Lado C: '))

# verificando se é triangulo
if (ladoA + ladoB) < ladoC or (ladoA + ladoC) < ladoB or (ladoB + ladoC) < ladoA:
    sys.exit('Valores informados não constituem um triangulo.')

cos_A = (-(ladoA ** 2) + ladoB ** 2 + ladoC ** 2) / (2 * ladoB * ladoB)
cos_B = (-(ladoB ** 2) + ladoA ** 2 + ladoC ** 2) / (2 * ladoA * ladoC) 
cos_C = (-(ladoC ** 2) + ladoA ** 2 + ladoB ** 2) / (2 * ladoA * ladoB)

cosA = (ladoB ** 2 + ladoC ** 2 - ladoA ** 2) / (2 * ladoB * ladoC)
cosB = (ladoA ** 2 + ladoC ** 2 - ladoB ** 2) / (2 * ladoA * ladoC)
cosC = (ladoA ** 2 + ladoB ** 2 - ladoC ** 2) / (2 * ladoA * ladoB)

print(f'cosA: {cos_A}\ncosB: {cos_B}\ncosC: {cos_C}\n')
print(f'cosA: {cosA}\ncosB: {cosB}\ncosC: {cosC}\n')