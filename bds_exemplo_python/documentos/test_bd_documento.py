#coding: utf-8

import unittest
import bd_documento as doc


class TestCriarColecao(unittest.TestCase):

    def setUp(self):
        self.banco = doc.BancoDocumentos()

    def tearDown(self):
        del self.banco

    def test_criar_colecao_inexistente(self):
        self.banco.criar_colecao('pessoas')
        self.assertIn('pessoas', self.banco.colecoes)
        self.assertEqual(self.banco.contadores['pessoas'], 0)

    def test_criar_colecao_ja_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.assertRaises(ValueError, self.banco.criar_colecao, 'pessoas')


class TestExcluirColecao(unittest.TestCase):

    def setUp(self):
        self.banco = doc.BancoDocumentos()

    def tearDown(self):
        del self.banco

    def test_excluir_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.banco.excluir_colecao('pessoas')
        self.assertNotIn('pessoas', self.banco.colecoes)
        self.assertNotIn('pessoas', self.banco.contadores)

    def test_excluir_colecao_inexistente(self):
        self.assertRaises(ValueError, self.banco.excluir_colecao, 'pessoas')


class TestCriarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = doc.BancoDocumentos()

    def tearDown(self):
        del self.banco

    def test_criar_registro_com_dicionario_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        dicio = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        novo_id = self.banco.inserir('pessoas', dicio)
        reg = self.banco.colecoes['pessoas'][novo_id]
        self.assertEqual(reg['nome'], 'José')

    def test_criar_registro_com_dicionario_aninhado_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        dicio = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False, 'endereco':{'logradouro':'Praça Central', 'numero':'102A'}}
        novo_id = self.banco.inserir('pessoas', dicio)
        reg = self.banco.colecoes['pessoas'][novo_id]
        self.assertEqual(reg['endereco']['logradouro'], 'Praça Central')

    def test_criar_registro_com_dicionario_colecao_inexistente(self):
        dicio = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        self.assertRaises(ValueError, self.banco.inserir, 'pessoas', dicio)

    def test_criar_registro_com_json_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        # padrao json: aspas duplas, booleanos em minusculo
        json = '{"nome":"José", "idade":20, "saldo":50.32, "vip":false}'
        novo_id = self.banco.inserir('pessoas', json)
        reg = self.banco.colecoes['pessoas'][novo_id]
        self.assertEqual(reg['nome'], u'José')

    def test_criar_registro_com_json_aninhado_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        # padrao json: aspas duplas, booleanos em minusculo
        json = '{"nome":"José", "idade":20, "saldo":50.32, "vip":false, "endereco":{"logradouro":"Praça Central", "numero":"102A"}}'
        novo_id = self.banco.inserir('pessoas', json)
        reg = self.banco.colecoes['pessoas'][novo_id]
        self.assertEqual(reg['endereco']['logradouro'], u'Praça Central')

    def test_criar_registro_com_tipo_invalido_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        dados = [1, 2, 3]
        self.assertRaises(TypeError, self.banco.inserir, 'pessoas', dados)


class TestRecuperarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = doc.BancoDocumentos()

    def tearDown(self):
        del self.banco

    def test_recuperar_registro_indice_existente_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 1
        dicio_1 = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        self.banco.colecoes['pessoas'][1] = dicio_1
        dicio_2 = self.banco.recuperar('pessoas', 1)
        self.assertEqual(dicio_2['nome'], 'José')

    def test_recuperar_registro_colecao_inexistente(self):
        self.assertRaises(ValueError, self.banco.recuperar, 'pessoas', 1)

    def test_recuperar_registro_indice_inexistente_colecao_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.assertRaises(KeyError, self.banco.recuperar, 'pessoas', 10)


class TestBuscarRegistro(unittest.TestCase):

    def setUpParaAlguns(self):
        self.banco = doc.BancoDocumentos()
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        dicio = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        self.banco.contadores['pessoas'] += 1
        self.banco.colecoes['pessoas'][self.banco.contadores['pessoas']] = dicio
        dicio = {'nome':'João', 'idade':35, 'saldo':30.50, 'vip':True}
        self.banco.contadores['pessoas'] += 1
        self.banco.colecoes['pessoas'][self.banco.contadores['pessoas']] = dicio
        dicio = {'nome':'Maria', 'idade':30, 'saldo':120.40, 'vip':False}
        self.banco.contadores['pessoas'] += 1
        self.banco.colecoes['pessoas'][self.banco.contadores['pessoas']] = dicio

    def tearDown(self):
        del self.banco

    def test_buscar_registro_unico_param_texto(self):
        self.setUpParaAlguns()
        colec_id = self.banco.buscar('pessoas', 'nome', 'Maria')
        self.assertEqual(colec_id[0], 3)

    def test_buscar_registro_unico_param_int(self):
        self.setUpParaAlguns()
        colec_id = self.banco.buscar('pessoas', 'idade', 35)
        self.assertEqual(colec_id[0], 2)

    def test_buscar_registros_multiplos_param_boolean(self):
        self.setUpParaAlguns()
        colec_id = self.banco.buscar('pessoas', 'vip', False)
        self.assertIn(1, colec_id)
        self.assertIn(3, colec_id)

    def test_buscar_registro_colecao_existente(self):
        self.banco = doc.BancoDocumentos()
        self.assertRaises(ValueError, self.banco.buscar, 'pessoas', 'nome', 'Maria')


class TestAtualizarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = doc.BancoDocumentos()

    def tearDown(self):
        del self.banco

    def test_atualizar_registro_indice_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 1
        dicio = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        self.banco.colecoes['pessoas'][self.banco.contadores['pessoas']] = dicio
        self.banco.atualizar('pessoas', 1, 'saldo', 45.00)
        self.assertEqual(self.banco.colecoes['pessoas'][1]['saldo'], 45.00)

    def test_atualizar_registro_colecao_inexistente(self):
        self.assertRaises(ValueError, self.banco.atualizar, 'pessoas', 1, 'saldo', 45.00)

    def test_atualizar_registro_chave_inexistente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 1
        self.assertRaises(KeyError, self.banco.atualizar, 'pessoas', 1, 'saldo', 45.00)


class TestExcluirRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = doc.BancoDocumentos()

    def tearDown(self):
        del self.banco

    def test_excluir_registro_indice_existente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 1
        dicio_1 = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        self.banco.colecoes['pessoas'][1] = dicio_1
        self.banco.excluir('pessoas', 1)
        self.assertNotIn(1, self.banco.colecoes['pessoas'])

    def test_excluir_registro_colecao_inexisetente(self):
        self.assertRaises(ValueError, self.banco.excluir, 'pessoas', 1)

    def test_excluir_registro_indice_inexistente(self):
        self.banco.colecoes['pessoas'] = {}
        self.banco.contadores['pessoas'] = 1
        self.assertRaises(KeyError, self.banco.excluir, 'pessoas', 1)


if __name__=='__main__':
    unittest.main()
