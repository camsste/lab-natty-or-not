import unittest
import sys
import os

# Adiciona o src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ia_fisiculturismo.gerador_conteudo import GeradorConteudoFisiculturismo

class TestGeradorConteudo(unittest.TestCase):
    
    def setUp(self):
        self.gerador = GeradorConteudoFisiculturismo()
    
    def test_gerar_treino_retorna_string(self):
        resultado = self.gerador.gerar_treino()
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)
    
    def test_gerar_dica_nutricao_retorna_string(self):
        resultado = self.gerador.gerar_dica_nutricao()
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

if __name__ == '__main__':
    unittest.main()