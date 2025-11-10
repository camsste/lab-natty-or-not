from dataclasses import dataclass
from typing import List

@dataclass
class Exercicio:
    nome: str
    grupo_muscular: str
    equipamento: str

@dataclass
class Treino:
    tipo: str
    exercicios: List[Exercicio]
    duracao: int
    series: int
    repeticoes: int

@dataclass
class Refeicao:
    nome: str
    alimentos: List[str]
    proteinas: int
    calorias: int

class DadosTreino:
    """Classe para gerenciar os dados do projeto"""
    
    def __init__(self):
        self.treinos = [
            "treino de peito e tríceps",
            "treino de costas e bíceps", 
            "treino de pernas e ombros",
            "treino full body",
            "treino de força máxima"
        ]
        
        self.exercicios = {
            "peito": ["supino reto", "supino inclinado", "crucifixo", "flexão"],
            "costas": ["barra fixa", "remada curvada", "puxada alta", "serrote"],
            "pernas": ["agachamento", "leg press", "cadeira extensora", "stiff"],
            "ombros": ["desenvolvimento", "elevação lateral", "remada alta"],
            "braços": ["rosca direta", "tríceps testa", "paralelas"]
        }
        
        self.dicas_treino = [
            "Mantenha a forma correta para evitar lesões",
            "Progressão de carga é fundamental",
            "Descanse adequadamente entre os treinos",
            "Hidrate-se bem durante o exercício",
            "Foque na mente-músculo"
        ]
        
        self.alimentos = [
            "frango grelhado", "batata doce", "ovos", "aveia", "brócolis",
            "arroz integral", "atum", "whey protein", "banana", "abacate"
        ]
        
        self.refeicoes = [
            "café da manhã", "lanche da manhã", "almoço", "lanche da tarde", "janta", "ceia"
        ]