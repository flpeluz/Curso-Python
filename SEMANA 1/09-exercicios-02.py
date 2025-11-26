
# Exercício:

# Encontrar o preço de um produto digitado pelo usuário:


preços = [1500, 1000, 800, 2000 ]
lista_produtos = ["celular", "camera", "fone de ouvido", "monitor"]

produto = input("Digite um produto: ").lower()

if produto in lista_produtos:
    print("produto encontrado!")
    posição = lista_produtos.index(produto)
    print("Produto:", produto)
    print("Preço:", preços[posição])
else:
    print("Produto não cadastrado!")



# Construa um Menu de opções:

preços = [1500, 1000, 800, 2000 ]
lista_produtos = ["celular", "camera", "fone de ouvido", "monitor"]

opção = int(input("ESCOLHA UMA OPÇÃO:"
      "\n1- Consultar preço de um produto:"
      "\n2- Listar produtos cadastrados:"
      "\n3- Cadastrar novo produto:"
      "\n4- Sair\n"))

if opção == 1:
    produto = input("Digite o produto: ").lower()
    if produto in lista_produtos:
        posição = lista_produtos.index(produto)
        print("Produto: ", produto)
        print("Preço: R$", preços[posição])

if opção == 2:
   for i in range(len(lista_produtos)):
        produto = lista_produtos[i]
        preço = preços[i]
        print(f"{i + 1} - {lista_produtos[i]} - R$ {preços[i]:.2f}")


if opção == 3:
    novo_produto = input("Digite novo produto: ").lower()
    novo_preço = int(input("Digite o preço do novo produto: "))
    lista_produtos.append(novo_produto)
    preços.append(novo_preço)
    print(lista_produtos)
    print(preços)
    print("\nProduto cadastrado com sucesso!\n")

if opção == 4:
    print("\nSaindo...\n")