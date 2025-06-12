strPalavra = input('Digite a palavra desejada: ')
intDeslocamento = int(input('Deslocamento Desejado: '))

strCifra = ''

print(f'Cifra com deslocamento {intDeslocamento}: ', end='')

for contador in range(0, len(strPalavra)):
    strCifra = chr(ord(strPalavra[contador]) + intDeslocamento)
    print(strCifra, end='')