#coding: utf-8

import unittest
import bd_big_table as bt


def preparar_um_registro(banco):
    banco.tabelas['pessoas'] = {}
    banco.tabelas['pessoas']['chave_1'] = {'alfa': 'textão', 'bravo': 42, 'charlie': 3.14}

def preparar_tres_registros(banco):
    banco.tabelas['pessoas'] = {}
    banco.tabelas['pessoas']['chave_1'] = {'alfa': 'textão', 'bravo': 42, 'charlie': 3.14}
    banco.tabelas['pessoas']['chave_2'] = {'alfa': 'outro textão', 'bravo': 42, 'delta': 1024}
    banco.tabelas['pessoas']['chave_3'] = {'alfa': 'outro textão', 'bravo': 0, 'charlie': 6.02}

class TestCriarTabela(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_criar_tabela_nao_existente(self):
        self.banco.criar_tabela('pessoas')
        self.assertIn('pessoas', self.banco.tabelas)

    def test_criar_tabela_ja_existente(self):
        self.banco.tabelas['pessoas'] = {}
        self.assertRaises(ValueError, self.banco.criar_tabela, 'pessoas')

# --------------------

class TestExcluirTabela(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_excluir_tabela_existente(self):
        self.banco.tabelas['pessoas'] = {}
        self.banco.excluir_tabela('pessoas')
        self.assertNotIn('pessoas', self.banco.tabelas)

    def test_excluir_tabela_nao_existente(self):
        self.assertRaises(ValueError, self.banco.excluir_tabela, 'pessoas')

# --------------------

class TestCriarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_criar_registro_tabela_nao_existe(self):
        self.assertRaises(ValueError, self.banco.inserir, 'pessoas', 'chave_1', {'alfa': 'textão'})

    def test_criar_registro_tabela_existe_chave_nao_existe(self):
        preparar_um_registro(self.banco)
        self.assertEqual(self.banco.tabelas['pessoas']['chave_1']['alfa'], 'textão')
        self.assertEqual(self.banco.tabelas['pessoas']['chave_1']['bravo'], 42)

    def test_criar_registro_tabela_existe_chave_existe(self):
        self.banco.tabelas['pessoas'] = {}
        self.banco.tabelas['pessoas']['chave_1'] = {}
        self.assertRaises(KeyError, self.banco.inserir, 'pessoas', 'chave_1', {'alfa': 'textão'})

# --------------------

class TestRecuperarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_recuperar_registro_tabela_nao_existe(self):
        self.assertRaises(ValueError, self.banco.recuperar, 'pessoas', 'chave_1', 'alfa')

    def test_recuperar_registro_tabela_existe_chave_existe(self):
        preparar_um_registro(self.banco)
        dados = self.banco.recuperar('pessoas', 'chave_1')
        self.assertEqual(dados['alfa'], 'textão')
        self.assertEqual(dados['bravo'], 42)

    def test_recuperar_registro_tabela_existe_chave_nao_existe(self):
        self.banco.tabelas['pessoas'] = {}
        self.banco.tabelas['pessoas']
        self.assertRaises(KeyError, self.banco.recuperar, 'pessoas', 'chave_1')

    def test_recuperar_registro_parcial_tabela_existe_chave_existe_colunas_existem(self):
        preparar_um_registro(self.banco)
        dados = self.banco.recuperar('pessoas', 'chave_1', ['charlie', 'bravo'])
        self.assertEqual(dados['bravo'], 42)
        self.assertEqual(dados['charlie'], 3.14)
        self.assertNotIn('alfa', dados)

    def test_recuperar_registro_parcial_tabela_existe_chave_existe_coluna_nao_existe(self):
        preparar_um_registro(self.banco)
        dados = self.banco.recuperar('pessoas', 'chave_1', ['nao_existe', 'bravo'])
        self.assertEqual(dados['bravo'], 42)
        self.assertEqual(dados['nao_existe'], None)

# --------------------

class TestAtualizarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_atualizar_registro_tabela_nao_existe(self):
        self.assertRaises(ValueError, self.banco.atualizar, 'pessoas', 'chave_1', {'alfa': 'textão'})

    def test_atualizar_registro_tabela_existe_chave_nao_existe(self):
        self.banco.tabelas['pessoas'] = {}
        self.assertRaises(KeyError, self.banco.atualizar, 'pessoas', 'chave_1', {'alfa': 'textão'})

    def test_atualizar_registro_tabela_existe_chave_existe(self):
        preparar_um_registro(self.banco)
        dados = {'alfa': 'novo textão', 'charlie': None, 'delta': 1024}
        self.banco.atualizar('pessoas', 'chave_1', dados)
        self.assertEqual(self.banco.tabelas['pessoas']['chave_1']['alfa'], 'novo textão')
        self.assertEqual(self.banco.tabelas['pessoas']['chave_1']['bravo'], 42)
        self.assertEqual(self.banco.tabelas['pessoas']['chave_1']['charlie'], None)
        self.assertEqual(self.banco.tabelas['pessoas']['chave_1']['delta'], 1024)

# --------------------

class TestExcluirRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_excluir_registro_tabela_nao_existe(self):
        self.assertRaises(ValueError, self.banco.excluir, 'pessoas', 'chave_1')

    def test_excluir_registro_tabela_existe_chave_existe(self):
        preparar_um_registro(self.banco)
        self.banco.excluir('pessoas', 'chave_1')
        self.assertNotIn('chave_1', self.banco.tabelas['pessoas'])

    def test_excluir_registro_tabela_existe_chave_nao_existe(self):
        self.banco.tabelas['pessoas'] = {}
        self.assertRaises(KeyError, self.banco.excluir, 'pessoas', 'chave_1')

    def test_excluir_colunas_existentes(self):
        preparar_um_registro(self.banco)
        self.banco.excluir('pessoas', 'chave_1', ['alfa', 'charlie', 'nao_existe'])
        self.assertIn('chave_1', self.banco.tabelas['pessoas'])
        self.assertIn('bravo', self.banco.tabelas['pessoas']['chave_1'])
        self.assertNotIn('alfa', self.banco.tabelas['pessoas']['chave_1'])
        self.assertNotIn('chalie', self.banco.tabelas['pessoas']['chave_1'])
        self.assertNotIn('nao_existe', self.banco.tabelas['pessoas']['chave_1'])

# --------------------

class TestBuscarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = bt.BancoBigTable()

    def tearDown(self):
        del self.banco

    def test_buscar_registro_tabela_nao_existe(self):
        self.assertRaises(ValueError, self.banco.buscar, 'pessoas', 'alfa', 'textão')

    def test_buscar_registro_tabela_existe_coluna_valor_existem(self):
        preparar_tres_registros(self.banco)
        chaves = self.banco.buscar('pessoas', 'bravo', 42)
        self.assertEqual(len(chaves), 2)
        self.assertIn('chave_1', chaves)
        self.assertIn('chave_2', chaves)

    def test_buscar_registro_tabela_existe_coluna_valor_nao_existem(self):
        preparar_tres_registros(self.banco)
        chaves = self.banco.buscar('pessoas', 'alfa', 'nada')
        self.assertEqual(len(chaves), 0)

    def test_buscar_todas_chaves_tabela_existe_registros_existem(self):
        preparar_tres_registros(self.banco)
        chaves = self.banco.buscar('pessoas')
        self.assertEqual(len(chaves), 3)
        self.assertIn('chave_1', chaves)
        self.assertIn('chave_2', chaves)
        self.assertIn('chave_3', chaves)

# --------------------

if __name__=='__main__':
    unittest.main()
