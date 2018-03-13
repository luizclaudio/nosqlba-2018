#coding: utf-8

class BancoChaveValor():

    def __init__(self):
        self.registros = {}

    def inserir(self, chave, valor):
        if chave not in self.registros:
            self.registros[chave] = valor
        else:
            raise ValueError('Chave já existe.')

    def recuperar(self, chave):
        return self.registros[chave]

    def atualizar(self, chave, valor):
        if chave in self.registros:
            self.registros[chave] = valor
        else:
            raise KeyError('Chave não encontrada.')

    def excluir(self, chave):
        del self.registros[chave]