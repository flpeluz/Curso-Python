# ovos = input('Tem ovos? (sim/não): ').lower()
# if ovos == 'sim':
#     print('Vê 6 pães!')

# else:
#     print('Vê 10 pães!')




lista_ptodutos = ["notebook", "tablet", "smartphone"]
lista_preços = [2500, 1500, 2000]
indice = 0
produto = input('Digite o nome do produto: ').lower()

if produto in lista_ptodutos:
    print('Produto em estoque!')
    produto = lista_ptodutos.index(produto)
    print(f'{lista_ptodutos[produto]} : R$ {lista_preços[produto]}')

else:
    print('Produto não cadastrado!')
    print('Deseja cadastrar o produto?')
    cadastro = input('Sim ou Não: ').lower()

    if cadastro == 'sim':
        novoproduto = input('Digite o nome do produto: ').lower()
        lista_ptodutos.append(novoproduto)
        novopreço = input('Digite o preço do produto: R$ ')
        lista_preços.append(novopreço)
        print(f'Produtos: {lista_ptodutos}\nPreço:{lista_preços}')
    else:
        print('Saindo do sistema...')