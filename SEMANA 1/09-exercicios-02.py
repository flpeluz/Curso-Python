
# Exercício:

# Encontrar o preço de um produto digitado pelo usuário:


preços = [1500, 1000, 800, 2000 ]
lista_produtos = ["celular", "camera", "fone de ouvido", "monitor"]
indice = 0

produto = input("Digite um produto: ").lower()

if produto in lista_produtos:
    print("produto encontrado!")
    posição = lista_produtos.index(produto)
    print("Produto:", produto)
    print("Preço:", preços[posição])
else:
    print("Produto não cadastrado!")