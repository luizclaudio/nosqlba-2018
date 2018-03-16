#coding: utf-8

import unittest
import bd_grafo as grafo

def inserir_registros_para_teste(banco):
    banco.criar_colecao('pessoas')
    banco.inserir('pessoas', {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False})
    banco.criar_colecao('bandas')
    banco.inserir('bandas', {'nome':'Iron Maiden', 'origem':'UK', 'genero':'Heavy Metal'})

def inserir_muitos_registros_para_teste(banco):
    banco.criar_colecao('pessoas')
    banco.inserir('pessoas', {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False})
    banco.inserir('pessoas', {'nome':'João', 'idade':35, 'saldo':30.50, 'vip':True})
    banco.inserir('pessoas', {'nome':'Maria', 'idade':30, 'saldo':120.40, 'vip':False})
    banco.criar_colecao('bandas')
    banco.inserir('bandas', {'nome':'Iron Maiden', 'origem':'UK', 'genero':'Heavy Metal'})
    banco.inserir('bandas', {'nome':'Capital Inicial', 'origem':'Brasil', 'genero':'Rock Brasil'})
    banco.inserir('bandas', {'nome':'The Offspring', 'origem':'USA', 'genero':'Punk Rock'})

def inserir_aresta_para_teste(banco):
    banco.contador_arestas = 1
    banco.arestas[1] = {
        'colecao_origem':'pessoas', 'indice_origem':1,
        'colecao_destino':'bandas', 'indice_destino':1,
        'tipo':'curte', 'valor':None}

def inserir_muitas_arestas_para_teste(banco):
    banco.contador_arestas = 6
    banco.arestas[1] = {
        'colecao_origem':'pessoas', 'indice_origem':1,
        'colecao_destino':'pessoas', 'indice_destino':2,
        'tipo':'segue', 'valor':None}
    banco.arestas[2] = {
        'colecao_origem':'pessoas', 'indice_origem':1,
        'colecao_destino':'pessoas', 'indice_destino':3,
        'tipo':'segue', 'valor':None}
    banco.arestas[3] = {
        'colecao_origem':'pessoas', 'indice_origem':2,
        'colecao_destino':'pessoas', 'indice_destino':3,
        'tipo':'segue', 'valor':None}
    banco.arestas[4] = {
        'colecao_origem':'pessoas', 'indice_origem':1,
        'colecao_destino':'bandas', 'indice_destino':1,
        'tipo':'curte', 'valor':None}
    banco.arestas[5] = {
        'colecao_origem':'pessoas', 'indice_origem':1,
        'colecao_destino':'bandas', 'indice_destino':2,
        'tipo':'curte', 'valor':None}
    banco.arestas[6] = {
        'colecao_origem':'pessoas', 'indice_origem':2,
        'colecao_destino':'bandas', 'indice_destino':2,
        'tipo':'curte', 'valor':None}


class TestCriarAresta(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_criar_aresta_inexistente(self):
        indice = self.banco.criar_aresta('pessoas', 1, 'bandas', 1, 'curte') # José curte Iron Maiden
        self.assertIn(indice, self.banco.arestas)
        self.assertEqual(self.banco.arestas[indice]['colecao_origem'], 'pessoas')
        self.assertEqual(self.banco.arestas[indice]['colecao_destino'], 'bandas')

    def test_criar_aresta_existente(self):
        inserir_aresta_para_teste(self.banco)
        self.assertRaises(ValueError, self.banco.criar_aresta, 'pessoas', 1, 'bandas', 1, 'curte')

    def test_criar_aresta_indice_origem_inexistente(self):
        self.assertRaises(KeyError, self.banco.criar_aresta, 'pessoas', 2, 'bandas', 1, 'curte')

    def test_criar_aresta_colecao_inexistente(self):
        self.assertRaises(ValueError, self.banco.criar_aresta, 'pessoas', 1, 'artistas', 1, 'curte')


class TestRecuperarAresta(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_recuperar_aresta_existente(self):
        inserir_aresta_para_teste(self.banco)
        aresta = self.banco.recuperar_aresta(1)
        self.assertEqual(aresta['colecao_origem'], 'pessoas')
        self.assertEqual(aresta['colecao_destino'], 'bandas')

    def test_recuperar_aresta_inexistente(self):
        self.assertRaises(KeyError, self.banco.recuperar_aresta, 2)


class TestBuscarAresta(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_buscar_aresta_existente(self):
        inserir_aresta_para_teste(self.banco)
        indice = self.banco.buscar_aresta('pessoas', 1, 'bandas', 1, 'curte')
        self.assertEqual(indice, 1)

    def test_buscar_aresta_inexistente(self):
        indice = self.banco.buscar_aresta('pessoas', 1, 'bandas', 1, 'curte')
        self.assertIsNone(indice)


class TestAlterarAresta(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_alterar_aresta_existente(self):
        self.banco.contador_arestas += 1
        self.banco.arestas[self.banco.contador_arestas] = {
            'colecao_origem':'pessoas', 'indice_origem':1,
            'colecao_destino':'bandas', 'indice_destino':1,
            'tipo':'curte', 'valor':'MUITO'}
        self.banco.alterar_aresta(1, 'POUCO')
        self.assertEqual(self.banco.arestas[1]['valor'], 'POUCO')

    def test_alterar_aresta_inexistente(self):
        self.assertRaises(KeyError, self.banco.alterar_aresta, 1, 'POUCO')


class TesteExcluirAresta(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_excluir_aresta_existente(self):
        inserir_aresta_para_teste(self.banco)
        self.banco.excluir_aresta(1)
        self.assertNotIn(1, self.banco.arestas)

    def test_excluir_aresta_inexistente(self):
        self.assertRaises(KeyError, self.banco.excluir_aresta, 1)


class TesteBuscarVerticesDestino(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_muitos_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_buscar_vertices_destino_mesma_colecao(self):
        inserir_muitas_arestas_para_teste(self.banco)
        vertices = self.banco.buscar_vertices_destino('pessoas', 1, 'segue')
        self.assertEqual(len(vertices), 2)
        self.assertIn(('pessoas', 2), vertices)
        self.assertIn(('pessoas', 3), vertices)

    def test_buscar_vertices_destino_outra_colecao(self):
        inserir_muitas_arestas_para_teste(self.banco)
        vertices = self.banco.buscar_vertices_destino('pessoas', 1, 'curte')
        self.assertEqual(len(vertices), 2)
        self.assertIn(('bandas', 1), vertices)
        self.assertIn(('bandas', 2), vertices)


class TesteBuscarVerticesOrigem(unittest.TestCase):

    def setUp(self):
        self.banco = grafo.BancoGrafo()
        inserir_muitos_registros_para_teste(self.banco)

    def tearDown(self):
        del self.banco

    def test_buscar_vertices_origem_mesma_colecao(self):
        inserir_muitas_arestas_para_teste(self.banco)
        vertices = self.banco.buscar_vertices_origem('pessoas', 3, 'segue')
        self.assertEqual(len(vertices), 2)
        self.assertIn(('pessoas', 1), vertices)
        self.assertIn(('pessoas', 2), vertices)

    def test_buscar_vertices_origem_outra_colecao(self):
        inserir_muitas_arestas_para_teste(self.banco)
        vertices = self.banco.buscar_vertices_origem('bandas', 2, 'curte')
        self.assertEqual(len(vertices), 2)
        self.assertIn(('pessoas', 1), vertices)
        self.assertIn(('pessoas', 2), vertices)

if __name__=='__main__':
    unittest.main()