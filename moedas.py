money = float(input('Quanto dinheiro vc tem na carteira? '))

conversao_dolar = money / 3.91 
conversao_euro = money / 4.45 
conversao_iene = money / 0.035 


print('Com {} reais voce consegue comprar {} dolares'.format(money,conversao_dolar))
print('\n')
print('Com {} reais voce pode comprar {} euros'.format(money,conversao_euro))
print('\n')
print('Com {} rais voce pode comprar {} ienes'.format(money,conversao_iene))


