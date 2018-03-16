#coding: utf-8

from bd_documento import BancoDocumentos


class BancoGrafo(BancoDocumentos):

    def __init__(self):
        super().__init__()
        self.arestas = {}
        self.contador_arestas = 0

    def criar_aresta(self, colecao_origem, indice_origem, colecao_destino, indice_destino, tipo, valor=None):
        # provoca KeyError para indices inexistentes e ValueError para colecoes inexistentes
        if self.recuperar(colecao_origem, indice_origem) and self.recuperar(colecao_destino, indice_destino):
            aresta_existente = [a[1] for a in self.arestas.items() if
                a[1]['colecao_origem'] == colecao_origem and a[1]['indice_origem'] == indice_origem and
                a[1]['colecao_destino'] == colecao_destino and a[1]['indice_destino'] == indice_destino and
                a[1]['tipo'] == tipo]
            if not aresta_existente:
                self.contador_arestas += 1
                novo_indice = self.contador_arestas
                self.arestas[novo_indice] = {
                    'colecao_origem':colecao_origem, 'indice_origem':indice_origem,
                    'colecao_destino':colecao_destino, 'indice_destino':indice_destino,
                    'tipo':tipo, 'valor':valor}
                return novo_indice
            else:
                raise ValueError('Aresta já existe.')

    def recuperar_aresta(self, indice):
        return self.arestas[indice] # deixa passar KeyError para indice inexistente

    def buscar_aresta(self, colecao_origem, indice_origem, colecao_destino, indice_destino, tipo):
        indice = None
        indices = [a[0] for a in self.arestas.items() if
            a[1]['colecao_origem'] == colecao_origem and a[1]['indice_origem'] == indice_origem and
            a[1]['colecao_destino'] == colecao_destino and a[1]['indice_destino'] == indice_destino and
            a[1]['tipo'] == tipo]
        if indices:
            indice = indices[0]
        return indice

    def alterar_aresta(self, indice, novo_valor):
        self.arestas[indice]['valor'] = novo_valor

    def excluir_aresta(self, indice):
        del self.arestas[indice]

    def buscar_vertices_destino(self, colecao, indice, tipo):
        return [(a[1]['colecao_destino'], a[1]['indice_destino']) for a in self.arestas.items() if
            a[1]['colecao_origem'] == colecao and
            a[1]['indice_origem'] == indice and
            a[1]['tipo'] == tipo]

    def buscar_vertices_origem(self, colecao, indice, tipo):
        return [(a[1]['colecao_origem'], a[1]['indice_origem']) for a in self.arestas.items() if
            a[1]['colecao_destino'] == colecao and
            a[1]['indice_destino'] == indice and
            a[1]['tipo'] == tipo]