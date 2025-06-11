strTexto = input('Digite um texto: ')

intPosicao = 1

while intPosicao <= len(strTexto):
    print(strTexto[0:intPosicao])
    intPosicao += 1