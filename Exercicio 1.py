preco = float(input('Preço do produto: '))
p = float(input('Desconto do produto: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O Preço do produto {}. Desconto de {}%.'.format(preco, p))
print('o valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto,final))