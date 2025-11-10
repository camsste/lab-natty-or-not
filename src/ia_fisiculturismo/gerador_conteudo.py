import random

class GeradorConteudoFisiculturismo:
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
        
        self.dicas = [
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
    
    def gerar_treino(self):
        """Gera um treino de fisiculturismo aleatório"""
        treino_escolhido = random.choice(self.treinos)
        duracao = random.randint(45, 90)
        series = random.randint(3, 5)
        repeticoes = random.randint(8, 12)
        
        # Seleciona exercícios baseados no tipo de treino
        exercicios_treino = self._selecionar_exercicios(treino_escolhido)
        dica_escolhida = random.choice(self.dicas)
        
        treino_gerado = self._formatar_treino(
            treino_escolhido, duracao, series, repeticoes, exercicios_treino, dica_escolhida
        )
        return treino_gerado
    
    def _selecionar_exercicios(self, tipo_treino):
        """Seleciona exercícios baseados no tipo de treino"""
        if "peito" in tipo_treino:
            return random.sample(self.exercicios["peito"], 3) + random.sample(self.exercicios["braços"], 2)
        elif "costas" in tipo_treino:
            return random.sample(self.exercicios["costas"], 3) + random.sample(self.exercicios["braços"], 2)
        elif "pernas" in tipo_treino:
            return random.sample(self.exercicios["pernas"], 4) + random.sample(self.exercicios["ombros"], 1)
        else:
            # Para treino full body ou força máxima
            todos_exercicios = []
            for grupo in self.exercicios.values():
                todos_exercicios.extend(grupo)
            return random.sample(todos_exercicios, 5)
    
    def _formatar_treino(self, tipo, duracao, series, repeticoes, exercicios, dica):
        """Formata o treino para exibição"""
        treino_texto = f"""
🏋️ **TREINO GERADO AUTOMATICAMENTE** 🏋️

📋 Tipo de Treino: {tipo.title()}
⏰ Duração: {duracao} minutos
🔢 Configuração: {series} séries de {repeticoes} repetições

💪 **Exercícios:**"""
        
        for i, exercicio in enumerate(exercicios, 1):
            treino_texto += f"\n   {i}. {exercicio.title()}"
        
        treino_texto += f"""

💡 **Dica do Dia:** {dica}

🔍 **Status Natty:** {'✅ Natural' if random.choice([True, False]) else '⚠️ Fake Natty?'}
"""
        return treino_texto
    
    def gerar_dica_nutricao(self):
        """Gera uma dica de nutrição aleatória"""
        refeicao = random.choice(self.refeicoes)
        alimentos = random.sample(self.alimentos, 2)
        proteinas = random.randint(30, 60)
        calorias = random.randint(400, 700)
        
        dica_nutricao = f"""
🥗 **DIETA DO DIA - RECOMENDAÇÃO NATTY** 🥗

🍽️ {refeicao.title()}: 
   • {alimentos[0]} + {alimentos[1]}
   • {proteinas}g de proteína
   • Aprox. {calorias} calorias

💧 Hidratação: {random.randint(2, 4)}L de água
⚖️ Déficit/Superávit: {random.choice(['Déficit calórico', 'Manutenção', 'Superávit calórico'])}
"""
        return dica_nutricao
    
    def gerar_conteudo_completo(self):
        """Gera conteúdo completo (treino + nutrição)"""
        treino = self.gerar_treino()
        nutricao = self.gerar_dica_nutricao()
        
        return f"""
🎯 **PLANO COMPLETO DO DIA** 🎯
{treino}
{nutricao}
"""

