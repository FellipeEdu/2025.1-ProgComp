strPalavra = input('Digite a palavra desejada: ')
intDeslocamento = int(input('Deslocamento Desejado: '))

strCifra = ''

print(f'Cifra com deslocamento {intDeslocamento}: ', end='')

for letra in strPalavra: # de "in range(0, len(strPalavra))" para "in strPalavra"

    intString = ord(letra) + intDeslocamento # de "(strPalavra[letra])" para "ord(letra)"

    if (intString) > 126:
        intCorrecao = (intString - 127)
        if intCorrecao >= 33:
            strCifra = chr(intCorrecao)
        else:
            intCorrecao += 33
            strCifra = chr(intCorrecao)
    else:
        strCifra += chr(intString)

print(strCifra, end='') # agora com o print fora do FOR, exibindo de uma vez a strCifra