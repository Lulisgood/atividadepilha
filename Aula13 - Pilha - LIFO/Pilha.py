from Livro import Livro

class PilhaLivros:
    def __init__(self):
        self.topo = None

    def adicionar_livro(self, titulo, autor):
        novo = Livro(titulo, autor)
        novo.prox = self.topo
        self.topo = novo

    def remover_livro(self):
        if self.topo is not None:
            removido = self.topo
            self.topo = self.topo.prox
            return removido
        return None

    def imprimir_pilha(self):
        if self.topo is None:
            print("\nPilha vazia!")
            return

        print("\nPilha de Livros:")
        atual = self.topo
        while atual is not None:
            print(f"Título: {atual.titulo} - Autor: {atual.autor.nome}")
            atual = atual.prox
