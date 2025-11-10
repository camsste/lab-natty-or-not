"""
Exemplo básico de uso do gerador de conteúdo
"""
import sys
import os

# Adiciona o src ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ia_fisiculturismo.gerador_conteudo import GeradorConteudoFisiculturismo

def exemplo_rapido():
    print("🚀 EXEMPLO RÁPIDO - IA FISICULTURISMO")
    print("=" * 50)
    
    gerador = GeradorConteudoFisiculturismo()
    
    # Gera um treino
    print("\n1. 🏋️ TREINO GERADO:")
    print(gerador.gerar_treino())
    
    # Gera uma dica de nutrição
    print("\n2. 🥗 DICA DE NUTRIÇÃO:")
    print(gerador.gerar_dica_nutricao())

if __name__ == "__main__":
    exemplo_rapido()