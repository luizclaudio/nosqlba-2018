#coding: utf-8

import unittest
import bd_coluna as bdcol


def inserir_registros_para_teste(banco):
    banco.familias['pessoas'] = {}
    banco.contadores['pessoas'] = 3
    banco.familias['pessoas']['nome'] = {}
    banco.familias['pessoas']['idade'] = {}
    banco.familias['pessoas']['saldo'] = {}
    banco.familias['pessoas']['vip'] = {}
    banco.familias['pessoas']['nome'][('José',)] = [1]
    banco.familias['pessoas']['nome'][('João',)] = [2]
    banco.familias['pessoas']['nome'][('Maria',)] = [3]
    banco.familias['pessoas']['idade'][(20,)] = [1, 2]
    banco.familias['pessoas']['idade'][(30,)] = [3]
    banco.familias['pessoas']['saldo'][(50.32,)] = [1]
    banco.familias['pessoas']['saldo'][(30.50,)] = [2]
    banco.familias['pessoas']['saldo'][(120.40,)] = [3]
    banco.familias['pessoas']['vip'][(False,)] = [1, 3]
    banco.familias['pessoas']['vip'][(True,)] = [2]


class TestCriarFamilia(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_criar_familia_inexistente(self):
        self.banco.criar_familia('pessoas')
        self.assertIn('pessoas', self.banco.familias)
        self.assertEqual(self.banco.contadores['pessoas'], 0)

    def test_criar_familia_ja_existente(self):
        self.banco.familias['pessoas'] = {}
        self.assertRaises(ValueError, self.banco.criar_familia, 'pessoas')


class TestExcluirFamilia(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_excluir_familia_existente(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.banco.excluir_familia('pessoas')
        self.assertNotIn('pessoas', self.banco.familias)
        self.assertNotIn('pessoas', self.banco.contadores)

    def test_excluir_familia_inexistente(self):
        self.assertRaises(ValueError, self.banco.excluir_familia, 'pessoas')


class TestCriarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_criar_registro(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        nova_pessoa = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        novo_id = self.banco.inserir('pessoas', nova_pessoa)
        self.assertEqual(self.banco.familias['pessoas']['nome'][('José',)], [novo_id])
        self.assertEqual(self.banco.familias['pessoas']['saldo'][(50.32,)], [novo_id])
        self.assertEqual(self.banco.familias['pessoas']['vip'][(False,)], [novo_id])

    def test_criar_registros_valores_iguais(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        pessoa_1 = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        id_1 = self.banco.inserir('pessoas', pessoa_1)
        pessoa_2 = {'nome':'João', 'idade':20, 'saldo':30.50, 'vip':False}
        id_2 = self.banco.inserir('pessoas', pessoa_2)
        self.assertEqual(self.banco.familias['pessoas']['idade'][(20,)], [id_1, id_2])
        self.assertEqual(self.banco.familias['pessoas']['vip'][(False,)], [id_1, id_2])

    def test_criar_registro_familia_inexistente(self):
        nova_pessoa = {'nome':'José', 'idade':20, 'saldo':50.32, 'vip':False}
        self.assertRaises(ValueError, self.banco.inserir, 'pessoas', nova_pessoa)


class TestRecuperarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_recuperar_registro_familia_existente_indice_existente(self):
        inserir_registros_para_teste(self.banco)
        uma_pessoa = self.banco.recuperar('pessoas', 1)
        self.assertEqual(uma_pessoa['nome'], 'José')
        self.assertEqual(uma_pessoa['vip'], False)

    def test_recuperar_registro_familia_existente_indice_inexistente(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.assertRaises(ValueError, self.banco.recuperar, 'pessoas', 1)

    def test_recuperar_registro_familia_inexistente(self):
        self.assertRaises(ValueError, self.banco.recuperar, 'pessoas', 1)


class TestBuscarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_buscar_registro_unico_param_texto(self):
        inserir_registros_para_teste(self.banco)
        ids_encontrados = self.banco.buscar('pessoas', 'nome', 'José')
        self.assertEqual(ids_encontrados[0], 1)

    def test_buscar_registro_multiplos_param_inteiro(self):
        inserir_registros_para_teste(self.banco)
        ids_encontrados = self.banco.buscar('pessoas', 'idade', 20)
        self.assertEqual(ids_encontrados, [1, 2])

    def test_buscar_registro_multiplos_param_boolean(self):
        inserir_registros_para_teste(self.banco)
        ids_encontrados = self.banco.buscar('pessoas', 'vip', False)
        self.assertEqual(ids_encontrados, [1, 3])

    def test_buscar_registro_campo_inexistente(self):
        inserir_registros_para_teste(self.banco)
        self.assertRaises(ValueError, self.banco.buscar, 'pessoas', 'cnpj', '12345678000199')

    def test_buscar_registro_familia_inexistente(self):
        self.assertRaises(ValueError, self.banco.buscar, 'pessoas', 'nome', 'José')


class TestAtualizarRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_atualizar_registro_familia_existente_coluna_existente_indice_existente(self):
        inserir_registros_para_teste(self.banco)
        self.banco.atualizar('pessoas', 1, 'idade', 30)
        self.banco.familias['pessoas']['idade'][(20,)] = [2]
        self.banco.familias['pessoas']['idade'][(30,)] = [3, 1]

    def test_atualizar_registro_familia_inexistente(self):
        self.assertRaises(ValueError, self.banco.atualizar, 'pessoas', 1, 'idade', 30)

    def test_atualizar_registro_familia_existente_coluna_inexistente(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.assertRaises(ValueError, self.banco.atualizar, 'pessoas', 1, 'idade', 30)

    def test_atualizar_registro_familia_existente_coluna_existente_indice_inexistente(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.banco.familias['pessoas']['idade'] = {}
        self.banco.familias['pessoas']['idade'][(30,)] = [2, 3]
        self.assertRaises(ValueError, self.banco.atualizar, 'pessoas', 1, 'idade', 30)


class TestExcluirRegistro(unittest.TestCase):

    def setUp(self):
        self.banco = bdcol.BancoColuna()

    def tearDown(self):
        del self.banco

    def test_excluir_registro_familia_existente_indice_existente(self):
        inserir_registros_para_teste(self.banco)
        self.banco.excluir('pessoas', 1)
        self.assertNotIn (('José',), self.banco.familias['pessoas']['nome'])
        self.assertNotIn (1, self.banco.familias['pessoas']['idade'][(20,)])
        self.assertNotIn ((50.32,), self.banco.familias['pessoas']['saldo'])
        self.assertNotIn (1, self.banco.familias['pessoas']['vip'][(False,)])

    def test_excluir_registro_familia_existente_indice_inexistente(self):
        self.banco.familias['pessoas'] = {}
        self.banco.contadores['pessoas'] = 0
        self.assertRaises(ValueError, self.banco.excluir, 'pessoas', 1)

    def test_excluir_registro_familia_inexistente(self):
        self.assertRaises(ValueError, self.banco.excluir, 'pessoas', 1)


if __name__=='__main__':
    unittest.main()