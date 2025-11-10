import sys
import os

# Adiciona o diretório src ao Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from ia_fisiculturismo.gerador_conteudo import GeradorConteudoFisiculturismo

def main():
    gerador = GeradorConteudoFisiculturismo()
    
    print("🤖 IA GENERATIVA - FISICULTURISMO NATTY 🤖")
    print("=" * 50)
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Gerar Treino Automático")
        print("2 - Gerar Dica de Nutrição")
        print("3 - Gerar Conteúdo Completo")
        print("4 - Sair")
        
        opcao = input("\nDigite sua opção (1-4): ").strip()
        
        if opcao == "1":
            print("\n" + "="*40)
            print(gerador.gerar_treino())
            print("="*40)
            
        elif opcao == "2":
            print("\n" + "="*40)
            print(gerador.gerar_dica_nutricao())
            print("="*40)
            
        elif opcao == "3":
            print("\n" + "="*40)
            print(gerador.gerar_conteudo_completo())
            print("="*40)
            
        elif opcao == "4":
            print("\n💪 Até a próxima! #NattyOrNot")
            break
            
        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
