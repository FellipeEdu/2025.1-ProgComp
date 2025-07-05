import sys

PALAVRA_CHAVE = 'ANA A GRAMA'
palavra = ''
palavraNova = ''
letrasUsadas = ''
primeiraIteracao = True
tentativas = 6

# formatação inicial
print('JOGO DA FORCA\n')
#print('A palavra é: ')
for carac in PALAVRA_CHAVE:
    if carac != ' ': print('_', end=' ')
    else: print(end='  ')

print('\n~~~~~~~~~~~~~~~~~~~')

while palavraNova != PALAVRA_CHAVE:
    try:
        letraEscolhida = input('Digite uma letra: ').upper()

        if len(letraEscolhida) > 1:
            print('ERRO: Digite apenas uma letra.')
            continue

    except ValueError:
        print('ERRO: digite um valor válido.')

    except Exception as excecao:
        print(f'ERRO: {excecao}')
    
    else:
        if letraEscolhida in letrasUsadas:
            print('Letra já usada, digite de novo...\n')
            continue

        if letraEscolhida in PALAVRA_CHAVE:
            if primeiraIteracao == True:
                for letra in range(len(PALAVRA_CHAVE)):
                    if PALAVRA_CHAVE[letra] == letraEscolhida: palavraNova += PALAVRA_CHAVE[letra]
                    elif PALAVRA_CHAVE[letra] == ' ': palavraNova += ' '
                    else: palavraNova += '_'

                    primeiraIteracao = False
            else:
                for letra in range(len(PALAVRA_CHAVE)): 
                    if PALAVRA_CHAVE[letra] == letraEscolhida:
                        palavraNova += PALAVRA_CHAVE[letra] # AN
                    else:
                        palavraNova += palavra[letra] # 'A'; 'ANA'

            print(palavraNova)
            print(f'Tentativas restantes: {tentativas}')
            palavra = palavraNova # A-A--A-A ; ANA--A-A
            letrasUsadas += letraEscolhida
        
        else: # caso erre a letra
            if primeiraIteracao == True:
                for letra in range(len(PALAVRA_CHAVE)):
                    if PALAVRA_CHAVE[letra] == letraEscolhida: palavraNova += PALAVRA_CHAVE[letra]
                    elif PALAVRA_CHAVE[letra] == ' ': palavraNova += ' '
                    else: palavraNova += '_'

                    primeiraIteracao = False
            else:
                for letra in range(len(PALAVRA_CHAVE)): 
                    if PALAVRA_CHAVE[letra] == letraEscolhida:
                        palavraNova += PALAVRA_CHAVE[letra] # AN
                    else:
                        palavraNova += palavra[letra] # 'A'; 'ANA'

            print(palavraNova)            
            tentativas -= 1
            print(f'Errado!\nTentativas restantes: {tentativas}')
            palavra = palavraNova
            letrasUsadas += letraEscolhida

        if tentativas == 0:
            print(f'XXX DEU FORCA, VOCÊ PERDEU! XXX\nA palavra era: {PALAVRA_CHAVE}...')
            break

        if palavraNova != PALAVRA_CHAVE:
            palavraNova = '' # zera a variavel para a próxima execuçao do programa

            # advinhar a palavra
            while True:
                print('Deseja adivinhar a palavra?')
                adivinhar = input("Digite 'S' para Sim, 'N' para Não: ").upper()

                if adivinhar == 'S':
                    palavra = input('\nDigite a palavra: ').upper()
                    
                    if palavra == PALAVRA_CHAVE:
                        sys.exit(f'Você descobriu a palavra chave {PALAVRA_CHAVE}, parabéns!')
                    else:
                        sys.exit(f'Essa não é a palavra, você perdeu!\nA palavra era: {PALAVRA_CHAVE}...')
                elif adivinhar == 'N': break
                else:
                    print('ERRO: digite um valor válido.\n')
        print()

if tentativas > 0: # para caso perca, ele não exiba essa linha, apenas se ganhar
    print(f'Você descobriu a palavra chave {PALAVRA_CHAVE}, parabéns!')