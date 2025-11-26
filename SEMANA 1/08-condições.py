# ------ IF e ELSE -------

# Exemplo 1:

# Maior de Idade ou Menor de Idade:

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade") # INDENTAÇÃO = tab -> para dentro, indica que o que será mostrado está condicionado ao "if" (estrutura de hierarquia dentro do código)
else:
    print("Menor de idade")


# Exemplo 2:

# Lucro positivo ou negativo:

faturamento = int(input("Digite o Faturamento: "))
custo = int(input("Digite o Custo: "))
lucro = faturamento - custo

if lucro >= 0:
    print("Lucro de: ", lucro)

else:
    print("Prejuizo de: ", lucro)


# Exemplo 3: 

# Produto cadastrado ou  não:

produtos = ["iphone", "ipad", "ipod"]
novo_produto = input("Digite o produto: ").lower()

if novo_produto in produtos:
    print("Produto já cadastrado!")

else:
    print("Produto não cadastrado!\n")



# Exemplo 4:

# Caso produto não esteja cadastrado, deseja cadastrar? :


produtos = ["iphone", "ipad", "ipod"]
novo_produto = input("Digite o produto: ").lower()

if novo_produto in produtos:
    print("Produto já cadastrado!")

else:
    print("Produto não cadastrado!\n")
    cadastro = input("Deseja adicionar este produto a lista? Sim ou Não: ").lower()
    if cadastro == "sim":
        print("Produto cadastrado com sucesso!")
        produtos.append(novo_produto)
        print(produtos)

    else:
        print("ok!")




# ------ ELIF --------


# Exemplo 1:


vendas = 15000

if vendas >= 10000:
    bonus = 500

elif vendas >= 5000:
    bonus = 100

elif vendas >= 1000:
    bonus = 50

else:
    bonus = 0

print("Bonus: ", bonus)



# Exemplo 2:


vendas = int(input("Digite o valor das vendas: "))
vendas_da_empresa = int(input("Digite o valor das vendas da empresa: "))
meta_da_empresa = 500000

if vendas >= 10000 and vendas_da_empresa > meta_da_empresa:
    bonus = 500

elif vendas >= 5000 and vendas_da_empresa > meta_da_empresa:
    bonus = 100

elif vendas >= 1000 and vendas_da_empresa > meta_da_empresa:
    bonus = 50

else:
    bonus = 0

print("Bonus: ", bonus)