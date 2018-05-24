#coding: utf-8

import json


class BancoDocumentos():

    def __init__(self):
        self.colecoes = {}
        self.contadores = {}

    def criar_colecao(self, nome):
        if not nome in self.colecoes:
            self.colecoes[nome] = {}
            self.contadores[nome] = 0
        else:
            raise ValueError('Coleção já existe.')

    def excluir_colecao(self, colecao):
        if colecao in self.colecoes:
            del self.colecoes[colecao]
            del self.contadores[colecao]
        else:
            raise ValueError('Coleção desconhecida.')

    def inserir(self, colecao, dados):
        if colecao in self.colecoes:
            dicionario = None
            if isinstance(dados, dict):
                dicionario = dados
            elif isinstance(dados, str):
                dicionario = json.loads(dados)
            else:
                raise TypeError('Dados devem ser dicionário ou texto JSON válido.')
            self.contadores[colecao] += 1
            novo_indice = self.contadores[colecao]
            self.colecoes[colecao][novo_indice] = dicionario
            return novo_indice
        else:
            raise ValueError('Coleção desconhecida.')

    def recuperar(self, colecao, indice):
        if colecao in self.colecoes:
            return self.colecoes[colecao][indice] # deixa passar KeyError para indice inexistente
        else:
            raise ValueError('Coleção desconhecida.')

    def buscar(self, colecao, chave, valor):
        if colecao in self.colecoes:
            return [reg[0] for reg in self.colecoes[colecao].items() if reg[1][chave] == valor]
        else:
            raise ValueError('Coleção desconhecida.')

    def atualizar(self, colecao, indice, chave, valor):
        if colecao in self.colecoes:
            self.colecoes[colecao][indice][chave] = valor # deixa passar KeyError para indice inexistente
        else:
            raise ValueError('Coleção desconhecida.')

    def excluir(self, colecao, indice):
        if colecao in self.colecoes:
            del self.colecoes[colecao][indice] # deixa passar KeyError para indice inexistente
        else:
            raise ValueError('Coleção desconhecida.')
