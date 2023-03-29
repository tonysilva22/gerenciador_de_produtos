# Criação de uma lista vazia para armazenar os produtos
produtos = []

# Função para adicionar um novo produto à lista
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {"nome": nome, "descricao": descricao, "preco": preco}
    produtos.append(produto)
    print("Produto adicionado com sucesso!")

# Função para exibir todos os produtos na lista
def listar_produtos():
    for produto in produtos:
        print("Nome:", produto["nome"])
        print("Descrição:", produto["descricao"])
        print("Preço:", produto["preco"])
        print("-----------")

# Função para buscar um produto na lista pelo nome
def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ")
    for produto in produtos:
        if produto["nome"] == nome:
            print("Nome:", produto["nome"])
            print("Descrição:", produto["descricao"])
            print("Preço:", produto["preco"])
            return
    print("Produto não encontrado.")
def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in produtos:
        if produto["nome"] == nome:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in produtos:
        if produto["nome"] == nome:
            descricao = input("Digite a nova descrição do produto: ")
            preco = float(input("Digite o novo preço do produto: "))
            produto["descricao"] = descricao
            produto["preco"] = preco
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")        
def adicionar_produto():
    while True:
        nome = input("Digite o nome do produto: ")
        if nome:
            break
        print("Nome do produto é obrigatório.")
    while True:
        descricao = input("Digite a descrição do produto: ")
        if descricao:
            break
        print("Descrição do produto é obrigatória.")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Preço do produto deve ser um número.")
    produto = {"nome": nome, "descricao": descricao, "preco": preco}
    produtos.append(produto)
    print("Produto adicionado com sucesso!")
    
# Menu principal do gerenciador de produtos
while True:
    print("Escolha uma opção:")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Sair")
    opcao = int(input("Digite sua escolha: "))
    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        buscar_produto()
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente.")
