'''
   Fazer um programa que faça as seguintes operações.

   1) A partir do conteúdo do arquivo cotacao_dolar.csv gerar uma lista onde cada item
      dessa lista será uma sub-lista com os valores de cada linha do arquivo.

      a) Os valores estão separados por ";";
      b) Os dois primeiros valores são valores do tipo FLOAT;
      c) O terceiro valor é do tipo DATE;
      

   2) Gerar arquivos para cada ano. Salvar o arquivo com o mesmo nome do arquivo que 
      foi aberto na questão 1, adionando no final do nome o sufixo "_nnnn" onde "nnnn" 
      corresponde ao ano das cotações;


   3) Gerar arquivos por ano com as médias das cotações mensais. Salve os arquivos com 
      o nome "media_cotacao_nnnn.csv" onde "nnnn" corresponde ao ano. Cada linha do arquivo
      deverá ter o valor médio de compra, o valor médio de venda e o nome do mês e fixar os 
      valores com 4 casas decimais. Separe os valores da linha por ";";
'''
import os, sys, statistics; from datetime import datetime

# Obtendo o diretório onde o programa está salvo
strDir = os.path.dirname(__file__)

# Abrindo e lendo o arquivo
try:
   arqLeitura = open(f'{strDir}\\cotacao_dolar.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   lstCotacoes = list()
   lstCabecalho = arqLeitura.readline().strip().split(';')
   while True:
      # Lendo a linha e armazenando na variável
      strLinha = arqLeitura.readline().strip()   
      # Interrompe o laço quando não há conteúdo na linha (EOF)
      if not strLinha: break
      # Transforma a string em uma lista
      lstAux = [linha for linha in strLinha.split(';')]
      #lstAux = [float(i) if i.isdigit() else i for i in strLinha.split(';')]
      # Adicionando os dados na lista
      cotCompra = float(lstAux[0].replace(',','.'))
      cotVenda = float(lstAux[1].replace(',', '.'))
      dataCot = datetime.strptime(lstAux[2], '%d/%m/%Y').date()
      lstCotacoes.append([cotCompra, cotVenda, dataCot])

   arqLeitura.close()

# classificando lstCotacao pelo ano
lstCotacoes.sort(key=lambda cotacao: (cotacao[2].year, cotacao[2].month, cotacao[2].day))

print(lstCabecalho)
for cotacoes in lstCotacoes:
   print(f"{cotacoes[0]:.3f}, {cotacoes[1]:.3f}, {cotacoes[2].strftime('%d/%m/%Y')}")

for 

for cotacoesLinha in lstCotacoes:
   ano = cotacoesLinha[2].year
   arqEscrita = open(f'{strDir}\\cotacao_dolar_{ano}.csv', 'w', encoding='utf-8')
   arqEscrita.write(f'{lstCabecalho}\n')
   
   linha = ';'.join(str(i) for i in cotacoesLinha)
   arqEscrita.write(f'{linha}\n')

arqEscrita.close()