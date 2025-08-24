#Gerenciador de Lista de Compras

def exibir_menu():
    print("\nMenu")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")

def adicionar_item(list):
    item = input("Digite o nome do item a ser adicionado: ").strip()
    if item in list:
        print(f"O item '{item}' já está na lista.")
    else:
        list.append(item)
        print(f"Item '{item}' adicionado com sucesso")

def remover_item(list):
    item = input("Digite o nome do item a ser removido: ").strip()
    if item in list:
        list.remove(item)
        print(f"Item '{item}' removido com sucesso!")
    else:
        print(f"O item '{item}' não esta na lista.")

def listar_itens(list):
    if list:
        print("\nItens na lista de compras:")
        for i, item in enumerate(list, start=1):
            print(f"{i}. {item}")
    else:
        print("A lista de compras está vazia")

#Progrmaa principal

list_compras = []
while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            adicionar_item(list_compras)
        elif opcao == 2:
            remover_item(list_compras)
        elif opcao == 3:
            listar_itens(list_compras)
        elif opcao == 4:
            print("Encerrando o programa. Boa sorte com sua compras!")
            break
        else:
            print("opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um numero correspondente à opção")