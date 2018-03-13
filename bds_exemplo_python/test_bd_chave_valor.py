import unittest
import bd_chave_valor as cv


class TestCriarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = cv.BancoChaveValor()

    def tearDown(self):
        del self.banco

    def test_criar_registro_chave_inexistente(self):
        self.banco.inserir('a', 42)
        self.assertEqual(self.banco.registros['a'], 42)

    def test_criar_registro_chave_existente(self):
        self.banco.registros['a'] = 42
        self.assertRaises(ValueError, self.banco.inserir, 'a', 99)


class TestRecuperarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = cv.BancoChaveValor()

    def tearDown(self):
        del self.banco

    def test_recuperar_registro_chave_existente(self):
        self.banco.registros['a'] = 42
        val = self.banco.recuperar('a')
        self.assertEqual(val, 42)

    def test_recuperar_registro_chave_inexistente(self):
        self.assertRaises(KeyError, self.banco.recuperar, 'a')


class TestAtualizarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = cv.BancoChaveValor()

    def tearDown(self):
        del self.banco

    def test_atualizar_registro_chave_existente(self):
        self.banco.registros['a'] = 42
        self.banco.atualizar('a', 99)
        val = self.banco.registros['a']
        self.assertEqual(val, 99)

    def test_atualizar_registro_chave_inexistente(self):
        self.assertRaises(KeyError, self.banco.atualizar, 'a', 99)


class TestApagarRegistros(unittest.TestCase):

    def setUp(self):
        self.banco = cv.BancoChaveValor()

    def tearDown(self):
        del self.banco

    def test_apagar_registro_chave_existente(self):
        self.banco.registros['a'] = 42
        self.banco.excluir('a')
        self.assertNotIn('a', self.banco.registros)

    def test_apagar_registro_chave_inexistente(self):
        self.assertRaises(KeyError, self.banco.excluir, 'a')

if __name__=='__main__':
    unittest.main()
