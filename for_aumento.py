precos_produtos = [1000, 500, 250, 125, 60, 30, 15] #lista de preços
aumento = 0.05 #aumento de 5% -> 0.05


for preco in precos_produtos: #para cada preço na lista de preços
    novo_preco = preco * (1 + aumento)

    print(novo_preco)