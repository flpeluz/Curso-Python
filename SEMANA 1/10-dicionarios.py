dic_preços = {"celular":1500, "fone de ouvido":800, "camera":1200, "notebook":2000}

preço_celular = dic_preços["celular"]
print(preço_celular)

print(len(dic_preços)) # imprime o tamanho do dicionario (quantos iténs)

dic_preços["relogio"] = 1100 # para adicionar itens ao dicionário
print(dic_preços)

dic_preços.pop("relogio") # para excluir items do dicionario 
print(dic_preços)




# Exercício: 

# Procurar um produto no dicionario:

produto_procurado = input("Digite o produto: ").lower()
if produto_procurado in dic_preços:
    print("Produto cadastrado!")
    preço = dic_preços[produto_procurado]
    print(f"Produto: {produto_procurado}\nPreço: {preço}")
          
else:
    print("Produto não cadastrado!")