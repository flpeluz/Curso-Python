# -------- FOR ------------



# for i in range(10): #para quantas vezes o loop vai rodar
#     print("Loop: Você tá mandando bem demais!")



# ------ RANGE ----------


# Exemplo 1 :

# for i in range(0, 10): # indice sempre começa em 0
#     print(i)
# print()

# for i in range(0, 10):
#     print(i + 1) # indice + 1 -> para iniciar em 1 
# print()

for i in range(0, 10):
    print(f"No {i + 1}º Loop o número é: {i + 1}") # indice + 1 -> para iniciar em 1 
print()

# for i in range(0, 10, 2): # (inicio, fim, pula)
#     print (i) # para numeros pares de 2 em 2
# print()

# for i in range(0, 10, 2):
#     print (i + 1) # para numeros impares de 2 em 2

# for i in range(len(nome)): # len = tamanho da lista (conteudo da lista)
#     print(i + 1, nome[i]) # i = indice -> então i + 1 para que o nunero comece em 1 === caso use somente i a lista começa em 0



# Exemplo 2 :

# produto = ["iphone", "macbook", "ipad", "apple watch", "airpods"]

# preco = [7100, 11000, 5000, 3500, 1500]

# estoque = [6, 2, 3, 4, 2]

# faturamento = 0

# for item in produto:
#     print(item.capitalize()) # capitalize deixa tudo com inicial maiuscula

# for item in range(len(produto)):
#     print(item + 1, produto[item]) # indice produto

# for item in range(len(produto)):
#     print(produto[item], item + 1) # produto indice


# for para calculo de aumento:

# precos_produtos = [1000, 500, 250, 125, 60, 30, 15] #lista de preços
# aumento = 0.05 #aumento de 5% -> 0.05


# for preco in precos_produtos: #para cada preço na lista de preços
#     novo_preco = preco * (1 + aumento)

#     print(novo_preco)









# --------- ZIP -----------

# -------- UNIR LISTAS E FORMATAR ----------


# zip -> permite colocar duas listas entre parenteses

# nome = ["Felipe", "Patricia", "Miguel", "Theo", "Matheus", "Benjamim", "Guilherme"]

# idade = [37, 33, 10, 4, 12, 6, 11]

# numeros = [1, 2 , 3 , 4, 5, 6, 7, 8, 9, 10]


# for nome, idade in zip(nome, idade):
#     print(f"{nome}: {idade}")



# Exemplo 1 :

# for i, p in zip(produto, preco): # i= item v= valor ==== zip -> permite colocar duas listas entre parenteses
#     print(f"{i}: {p}")


# for i, v, e in zip(produto, preco, estoque): # i= item v= valor e= estoque ==== zip -> permite colocar duas ou mais listas entre parenteses
#     print(f"{i}: {v} - {e}")




# Exemplo 2 :

# nome = ["Felipe", "Patricia", "Miguel", "Theo", "Matheus", "Benjamim", "Guilherme"]

# idade = [37, 33, 10, 4, 12, 6, 11]

# for nome, idade in zip(nome, idade):
#     print(f"{nome}: {idade} anos")








# ------- SOMA --------



# Exemplo 1 :

# num = [1, 2]
# soma = sum(num)
# print(soma)


# Exemplo 2 :

# produto = ["iphone", "macbook", "ipad", "apple watch", "airpods"]

# preco = [7100, 11000, 5000, 3500, 1500]

# estoque = [6, 2, 3, 4, 2]

# resultado = []  # resultado do calculo "append" = [42600, 22000, 15000, 14000, 3000] 


# print("\nInventário da Loja:\n") # Mostra o título do documento

# for p, e in zip(preco, estoque):   # apresenta os valores a serem calculados
#     resultado.append(p * e)    # adiciona a lista [RESULTADO] o valor calculado

# soma = sum(resultado) # soma os valores dentro da lista "resultado"

# for i, p, e in zip(produto, preco, estoque):  # apresenta os itens que quero mostrar, no caso: "Produto, valor e quantidade"
#     print(f"\nProduto: {i}\nPreço: {p}\nQuantidade em estoque: {e}")  # mostra na formatação que eu quero

# print(f"\nValor Total em Produtos: {soma}\n")   # mostra ao final da lista o valor total dos produtos da loja.



# Exemplo 3 :

# produto = ["camisetas", "bermudas", "bonés", "jaquetas", "calças"]

# preços = [80, 120, 40, 200, 180]

# estoque = [20, 10, 15, 10, 14]

# resultado = [] # [1600, 1200, 600, 2000, 2520]

# print("\n- LOJA DO LUZ -\n")

# for p, e in zip(preços, estoque):
#     resultado.append(p * e)

# soma = sum(resultado)

# for p, pr, e in zip(produto, preços, estoque):
#     print(f"\nProduto: {p}\nPreço: R$ {pr}\nEstoque: {e}\n")

# print(f"O valor total em produtos: R$ {soma}\n")