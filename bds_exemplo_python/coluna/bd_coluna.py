#coding: utf-8

class BancoColuna():

    def __init__(self):
        self.familias = {}
        self.contadores = {}

    def criar_familia(self, nome_familia):
        if not nome_familia in self.familias:
            self.familias[nome_familia] = {}
            self.contadores[nome_familia] = 0
        else:
            raise ValueError('Famíla já existe.')

    def excluir_familia(self, nome_familia):
        if nome_familia in self.familias:
            del self.familias[nome_familia]
            del self.contadores[nome_familia]
        else:
            raise ValueError('Família desconhecida.')

    def inserir(self, nome_familia, registro):
        if nome_familia in self.familias:
            self.contadores[nome_familia] += 1
            novo_id = self.contadores[nome_familia]
            for nome_coluna, valor in registro.items():
                if nome_coluna not in self.familias[nome_familia]:
                    self.familias[nome_familia][nome_coluna] = {}
                if (valor,) not in self.familias[nome_familia][nome_coluna]:
                    self.familias[nome_familia][nome_coluna][(valor,)] = []
                self.familias[nome_familia][nome_coluna][(valor,)].append(novo_id)
            return novo_id
        else:
            raise ValueError('Família desconhecida.')

    def recuperar(self, nome_familia, indice):
        if nome_familia in self.familias:
            registro = {}
            indice_encontrado = False
            for coluna, valores_coluna in self.familias[nome_familia].items():
                for valor_coluna, vetor_indices in valores_coluna.items():
                    if indice in vetor_indices:
                        registro[coluna] = valor_coluna[0]
                        indice_encontrado = True
            if indice_encontrado:
                return registro
            else:
                raise ValueError('Índice não encontrado.')
        else:
            raise ValueError('Família desconhecida.')

    def buscar(self, nome_familia, nome_coluna, valor_coluna):
        if nome_familia in self.familias:
            if nome_coluna in self.familias[nome_familia]:
                if (valor_coluna,) in self.familias[nome_familia][nome_coluna]:
                    indices = self.familias[nome_familia][nome_coluna][(valor_coluna,)]
                else:
                    indices = []
                return indices
            else:
                raise ValueError('Coluna desconhecida.')
        else:
            raise ValueError('Família desconhecida.')

    def atualizar(self, nome_familia, indice, nome_coluna, novo_valor):
        if nome_familia in self.familias:
            if nome_coluna in self.familias[nome_familia]:
                for valor_coluna, vetor_indices in self.familias[nome_familia][nome_coluna].items():
                    if indice in vetor_indices:
                        if (novo_valor,) not in self.familias[nome_familia][nome_coluna]:
                            self.familias[nome_familia][nome_coluna][(novo_valor,)] = []
                        self.familias[nome_familia][nome_coluna][(novo_valor,)].append(indice)
                        self.familias[nome_familia][nome_coluna][valor_coluna].remove(indice)
                        return
                raise ValueError('Índice não encontrado.')
            else:
                raise ValueError('Coluna desconhecida.')
        else:
            raise ValueError('Família desconhecida.')

    def excluir(self, nome_familia, indice):
        if nome_familia in self.familias:
            indice_encontrado = False
            for coluna, valores_coluna in self.familias[nome_familia].items():
                chave_excluir = None
                for valor_coluna, vetor_indices in valores_coluna.items():
                    if indice in vetor_indices:
                        vetor_indices.remove(indice)
                        if len(vetor_indices) == 0:
                            chave_excluir = valor_coluna
                        indice_encontrado = True
                if chave_excluir:
                    del self.familias[nome_familia][coluna][chave_excluir]
            if not indice_encontrado:
                raise ValueError('Índice não encontrado.')
        else:
            raise ValueError('Família desconhecida.')