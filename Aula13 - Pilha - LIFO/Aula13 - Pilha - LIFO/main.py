from Autor import ListaAutores
from Pilha import PilhaLivros


listaAutores = ListaAutores()
pilha = PilhaLivros()

while True:
    print("\nMENU")
    print("1 - Adicionar Autor")
    print("2 - Adicionar Livro")
    print("3 - Remover Livro")
    print("4 - Imprimir Pilha de Livros")
    print("5 - Imprimir Lista de Autores")
    print("6 - Sair")

    opc = input("Escolha: ")

    if opc == "1":
        id_autor = int(input("ID do autor: "))
        nome_autor = input("Nome do autor: ")
        listaAutores.adicionar_autor(id_autor, nome_autor)
        print("Autor adicionado com sucesso!")

    elif opc == "2":
        titulo = input("Título do livro: ")
        nome_autor = input("Nome do autor: ")

        autor = listaAutores.buscar_autor(nome_autor)
        if autor is None:
            print("Autor não encontrado! Cadastre o autor primeiro.")
        else:
            pilha.adicionar_livro(titulo, autor)
            print("Livro adicionado na pilha!")

    elif opc == "3":
        removido = pilha.remover_livro()
        if removido:
            print(f"Livro removido: {removido.titulo}")
        else:
            print("A pilha está vazia!")

    elif opc == "4":
        pilha.imprimir_pilha()

    elif opc == "5":
        listaAutores.imprimir_autores()

    elif opc == "6":
        break

    else:
        print("Opção inválida!")
