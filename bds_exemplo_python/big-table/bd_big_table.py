#coding: utf-8

class BancoBigTable():

    def __init__(self):
        self.tabelas = {}

    def criar_tabela(self, nome_tabela):
        if not nome_tabela in self.tabelas:
            self.tabelas[nome_tabela] = {}
        else:
            raise ValueError('Tabela já existe.')

    def excluir_tabela(self, nome_tabela):
        if nome_tabela in self.tabelas:
            del self.tabelas[nome_tabela]
        else:
            raise ValueError('Tabela desconhecida.')

    def inserir(self, tabela, chave, dados):
        if tabela in self.tabelas:
            if not chave in self.tabelas[tabela]:
                self.tabelas[tabela][chave] = {} # provoca KeyError para tabela inexistente
                for k, v in dados.items():
                    self.tabelas[tabela][chave][k] = v
            else:
                raise KeyError('Chave já existe.')
        else:
            raise ValueError('Tabela desconhecida.')

    def recuperar(self, tabela, chave, colunas=[]):
        if tabela in self.tabelas:
            if not colunas:
                return self.tabelas[tabela][chave] # provoca KeyError para chave inexistente
            else:
                dados = {}
                for c in colunas:
                    if c in self.tabelas[tabela][chave]: # provoca KeyError para chave inexistente
                        dados[c] = self.tabelas[tabela][chave][c]
                    else:
                        dados[c] = None
                return dados
        else:
            raise ValueError('Tabela desconhecida.')

    def buscar(self, tabela, coluna=None, valor=None):
        if tabela in self.tabelas:
            if coluna and valor:
                encontradas = []
                for chave, dados in self.tabelas[tabela].items():
                    for k,v  in dados.items():
                        if k == coluna and v == valor:
                            encontradas.append(chave)
                return encontradas
            else:
                return self.tabelas[tabela].keys()
        else:
            raise ValueError('Tabela desconhecida.')

    def atualizar(self, tabela, chave, dados):
        if tabela in self.tabelas:
            for k, v in dados.items():
                self.tabelas[tabela][chave][k] = v # provoca KeyError para chave inexistente
        else:
            raise ValueError('Tabela desconhecida.')

    def excluir(self, tabela, chave, colunas=[]):
        if tabela in self.tabelas:
            if not colunas:
                del self.tabelas[tabela][chave] # provoca KeyError para chave inexistente
            else:
                for c in colunas:
                    if c in self.tabelas[tabela][chave]:
                        del self.tabelas[tabela][chave][c]
        else:
            raise ValueError('Tabela desconhecida.')
