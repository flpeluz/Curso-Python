lista_produtos = ["celular", "camera", "fone de ouvido", "monitor"]

produto = input("Digite um produto: ").lower()
if produto in lista_produtos:
    print("produto encontrado!")

else:
    print("Produto não cadastrado!")