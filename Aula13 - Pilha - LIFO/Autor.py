class Autor:
    def __init__(self, id, nome):
        self.id = int
        self.nome = string
        self.prox = None


class ListaAutores:
    def __init__(self):
        self.inicio = None

    def adicionar_autor(self, id, nome):
        novo = Autor(id, nome)

        
        if self.inicio is None:
            self.inicio = novo
            return novo

        anterior = None
        atual = self.inicio

        
        while atual is not None and atual.nome.lower() < nome.lower():
            anterior = atual
            atual = atual.prox

        if anterior is None:
            
            novo.prox = self.inicio
            self.inicio = novo
        else:
            
            novo.prox = atual
            anterior.prox = novo

        return novo

    def buscar_autor(self, nome):
        atual = self.inicio
        while atual is not None:
            if atual.nome.lower() == nome.lower():
                return atual
            atual = atual.prox
        return None

    def imprimir_autores(self):
        atual = self.inicio
        print("\nLista de Autores:")
        while atual is not None:
            print(f"ID: {atual.id} - Nome: {atual.nome}")
            atual = atual.prox
