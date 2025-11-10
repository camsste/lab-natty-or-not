"""
Exemplo avançado - Gerando conteúdo para redes sociais
"""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ia_fisiculturismo.gerador_conteudo import GeradorConteudoFisiculturismo

def gerar_conteudo_redes_sociais():
    gerador = GeradorConteudoFisiculturismo()
    
    print("📱 CONTEÚDO PARA REDES SOCIAIS")
    print("#LabDIONattyOrNot")
    print("=" * 50)
    
    for i in range(3):
        print(f"\n🎯 POST {i+1}:")
        print(gerador.gerar_conteudo_completo())
        print("\n" + "🔁 Compartilhe usando #LabDIONattyOrNot")
        print("-" * 50)

if __name__ == "__main__":
    gerar_conteudo_redes_sociais()