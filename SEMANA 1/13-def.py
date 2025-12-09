# ------- FUNÇÕES DEF ------------

# Função -> Bloco de código reutilizável
# Organização

# Como funciona:
    # def nome_da_funcao(parametros):
        # instrução1
        # instrução2
        # ...
        # return valor (opcional)

def calcular_imposto(valor):
    if valor <= 1000:
        imposto = valor * 0.1
    elif valor <= 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2

    return imposto

preço_produto1 = 2500
preçoproduto2 = 3500

imposto_produto1 = calcular_imposto(preço_produto1)
imposto_produto2 = calcular_imposto(preçoproduto2)

print(imposto_produto1)
print(imposto_produto2)



# # Def para Cadastrar Produtos

# produtos = ["iphone", "ipad", "ipod"]
# novo_produto = input("Digite o produto: ").lower()


# def cadastro_produtos():

#     if novo_produto in produtos:
#         print("Produto já cadastrado!")

#     else:
#         print("Produto não cadastrado!\n")
#         cadastro = input("Deseja adicionar este produto a lista? Sim ou Não: ").lower()
#         if cadastro == "sim":
#             print("Produto cadastrado com sucesso!")
#             produtos.append(novo_produto)
#             print(produtos)

#         else:
#             print("ok!")


# cadastro_produtos()