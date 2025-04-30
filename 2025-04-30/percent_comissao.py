# fazer um programa pra solicitar o valor de uma venda e
# o percentual da comissao e exibir o valor da comissao

valor_venda = float(input('digite o valor da venda (R$): '))
percentual = float(input('informe a comissao (%).....: '))

comissao = valor_venda * percentual / 100

print(f'O valor da comissao é R${comissao:.2f}')