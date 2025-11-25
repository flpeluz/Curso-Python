vendas = [1000, 200, 500, 300, 50, 400]
# indice    0    1    2    3    4   5

print(f"Primeira venda: {vendas[0]}") # -> valor do indice 0

total_vendas = sum(vendas)

print(f"Total de vendas: {total_vendas}")

quantidade = len(vendas)

print(f"Quantidade de vendas: {quantidade}")

valor_max = max(vendas)
valor_min = min(vendas)

print(f"Valor máximo vendido: {valor_max}")
print(f"Valor mínimo vendido: {valor_min}")

posição = vendas.index(500) # da a posição do index (indice) "2"

print(posição) 
print(vendas[2:])
print(vendas[:2])


produtos = ["iphone", "ipad", "airpod", "macbook"]

print("iphone" in produtos) # -> TRUE

print("apple watch" in produtos) # -> FALSE



# edita em 10% o preço do produto:

produtos = ["iphone", "ipad", "airpod", "macbook"]
preço = [7000, 4000, 1200, 10000]

novo_preço = preço[0] * 1.1 # -> para aumentar em 10% o preço = preço x ele mesmo + 10%
preço = novo_preço

# ------ OU ------

novo_preço = preço[0] * (1 + 0.1)
preço = novo_preço

print(preço)


# Adiciona um ítem as listas: 

produtos.append("apple watch")
preço.append(3000)

print(produtos)
print(preço)


# Remove um ítem as listas: 

produtos.remove("ipad") # -> remove pelo ítem (valor) dentro da lista
preço.pop(1) # -> remove pelo índice da lista

print(produtos)
print(preço)


# inserir produtos pela posição:

produtos.insert(1, "airpod") # -> insere ítem no indice 1

# Contar valores dentro de uma lista:

print(produtos)

print(f"Quantidade de Airpod: ", produtos.count("airpod"))


# Ordenar:

preço.sort() # -> ordem crescente
print(preço)

preço.sort(reverse=True) # -> ordem decrescente
print(preço)


