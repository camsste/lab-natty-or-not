import unittest
import sys
import os

# Adiciona o src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ia_fisiculturismo.modelos import DadosTreino, Exercicio, Treino, Refeicao

class TestModelos(unittest.TestCase):
    
    def setUp(self):
        """Configuração inicial para os testes"""
        self.dados = DadosTreino()
    
    def test_dados_treino_inicializacao(self):
        """Testa se DadosTreino é inicializado corretamente"""
        self.assertIsInstance(self.dados.treinos, list)
        self.assertGreater(len(self.dados.treinos), 0)
        
        self.assertIsInstance(self.dados.exercicios, dict)
        self.assertIn('peito', self.dados.exercicios)
        self.assertIn('costas', self.dados.exercicios)
        self.assertIn('pernas', self.dados.exercicios)
        self.assertIn('ombros', self.dados.exercicios)
        self.assertIn('braços', self.dados.exercicios)
    
    def test_dados_treino_conteudo(self):
        """Testa o conteúdo dos dados de treino"""
        # Verifica se há exercícios em cada grupo muscular
        for grupo, exercicios in self.dados.exercicios.items():
            self.assertIsInstance(exercicios, list)
            self.assertGreater(len(exercicios), 0)
        
        # Verifica dicas de treino
        self.assertIsInstance(self.dados.dicas_treino, list)
        self.assertGreater(len(self.dados.dicas_treino), 0)
        
        # Verifica alimentos
        self.assertIsInstance(self.dados.alimentos, list)
        self.assertGreater(len(self.dados.alimentos), 0)
        
        # Verifica refeições
        self.assertIsInstance(self.dados.refeicoes, list)
        self.assertGreater(len(self.dados.refeicoes), 0)
    
    def test_exercicio_dataclass(self):
        """Testa a criação de objetos Exercicio"""
        exercicio = Exercicio(
            nome="Supino Reto",
            grupo_muscular="Peito",
            equipamento="Barra"
        )
        
        self.assertEqual(exercicio.nome, "Supino Reto")
        self.assertEqual(exercicio.grupo_muscular, "Peito")
        self.assertEqual(exercicio.equipamento, "Barra")
    
    def test_treino_dataclass(self):
        """Testa a criação de objetos Treino"""
        exercicios = [
            Exercicio("Supino Reto", "Peito", "Barra"),
            Exercicio("Crucifixo", "Peito", "Máquina")
        ]
        
        treino = Treino(
            tipo="Treino de Peito",
            exercicios=exercicios,
            duracao=60,
            series=4,
            repeticoes=10
        )
        
        self.assertEqual(treino.tipo, "Treino de Peito")
        self.assertEqual(len(treino.exercicios), 2)
        self.assertEqual(treino.duracao, 60)
        self.assertEqual(treino.series, 4)
        self.assertEqual(treino.repeticoes, 10)
    
    def test_refeicao_dataclass(self):
        """Testa a criação de objetos Refeicao"""
        refeicao = Refeicao(
            nome="Almoço",
            alimentos=["Frango", "Batata Doce", "Brócolis"],
            proteinas=35,
            calorias=500
        )
        
        self.assertEqual(refeicao.nome, "Almoço")
        self.assertEqual(len(refeicao.alimentos), 3)
        self.assertEqual(refeicao.proteinas, 35)
        self.assertEqual(refeicao.calorias, 500)

class TestIntegracaoModelos(unittest.TestCase):
    """Testes de integração entre os modelos"""
    
    def test_dados_com_exercicios(self):
        """Testa se os dados podem ser usados com a classe Exercicio"""
        dados = DadosTreino()
        
        # Cria exercícios a partir dos dados
        exercicios_peito = [
            Exercicio(nome=nome, grupo_muscular="Peito", equipamento="Variado")
            for nome in dados.exercicios['peito'][:2]
        ]
        
        self.assertEqual(len(exercicios_peito), 2)
        self.assertEqual(exercicios_peito[0].grupo_muscular, "Peito")

if __name__ == '__main__':
    # Executa todos os testes
    unittest.main()