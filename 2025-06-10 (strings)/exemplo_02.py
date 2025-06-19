strTexto = input('Digite um texto: ')

intPosicao = 0

while intPosicao < len(strTexto):
    print(strTexto[0:intPosicao + 1])
    intPosicao += 1